import logging
#DB
import pymongo
import settings
from eve import Eve
from bson.objectid import ObjectId

# Pdf process
import os
import hashlib
import urllib.request
import shutil
import time

TEST_URL_TO_DOWNLOAD = 'http://www.africau.edu/images/default/sample.pdf'

# checking is argument exists
def check_pdf(request, lookup):
	try:
		request.args['check_pdf']
	except Exception as e:
		return
	else:
		logging.info('Checking remote pdfs')
		process_pdf(request, lookup)

def process_pdf(request, lookup):
	# init db connection
	mongo_client = pymongo.MongoClient(settings.MONGO_URI)
	db = mongo_client.eve
	orders  = db.orders

	# get links of requested object
	parser_searches = orders.find_one({
		'_id': ObjectId(lookup['_id'])
	})['entities']['wp']['data']['parser_search']

	# if there is no links, stop function
	if len(parser_searches) < 1:
		logging.warning('Requested id (' + lookup['_id'] + ') has no any pdf to download')
		return

	# run through every parser_search item
	# index used in update query
	for idx, item in enumerate(parser_searches):

		logging.debug('Downloading from url: ' + item['value'])

		# response_pdf is raw response of urlopen
		# pdf_data is bytes read from response
		response_pdf = {}
		try:
			response_pdf = urllib.request.urlopen(item['value'])
		except Exception as e:
			logging.error('Cannot download pdf from url: ' + item['value'])
			logging.error(e)
			continue
		logging.debug('PDF downloaded')

		pdf_data = response_pdf.read()

		logging.debug('Checking hashsum')
		md5 = calc_md5(pdf_data)
		logging.debug('Hashsum is ' + md5)
		# if there is no downloaded field start saving immediately
		if 'downloaded' in item:
			# sort existing items just to be sure
			# and take first
			if sorted(item['downloaded'], key=lambda x: x['download_time'])[0]['filehash'] == md5:
				logging.debug('Hashsums is equal. Skipping')
				continue

		current_time = int(time.time())

		# create folder with object id
		if not os.path.exists(settings.PATH_TO_PDF_STORAGE + str(lookup['_id'])):
			os.makedirs(settings.PATH_TO_PDF_STORAGE + str(lookup['_id']))

		filename = str(lookup['_id']) + '/' + str(current_time) + '_' + response_pdf.url.split('/')[-1]
		logging.debug('Saving file to: ' + settings.PATH_TO_PDF_STORAGE + filename)

		# shutil methods does not work for some reason
		# using built-in file's methods
		out_file = open(settings.PATH_TO_PDF_STORAGE + filename, 'wb')
		out_file.write(pdf_data)
		out_file.close()

		logging.debug('Updating db')
		orders.update_one(
			{'_id': ObjectId(lookup['_id'])},
			{'$push': {
				'entities.wp.data.parser_search.' + str(idx) + '.downloaded': {
					'filepath': filename,
					'download_time': current_time,
					'filehash': md5
				}
			}}
		)
		logging.info('Updated')

def calc_md5(str):
	hash_md5 = hashlib.md5()
	hash_md5.update(str)
	return hash_md5.hexdigest()