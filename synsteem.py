# -*- coding: utf-8 -*-
"""
    Synergis Lab Synpat service API
    steem blockchain interaction module
    ~~~~~~~~~~~~~~~~~
    :license: BSD, see LICENSE for more details.
"""
import steem
import logging
import os
import settings
import web3tool

logging.basicConfig(format='%(asctime)s->%(levelname)s:[in %(filename)s:%(lineno)d]:%(message)s'
        , level=int(os.environ.get('EXO_LOGLEVEL',logging.DEBUG))
    )


def after_fetch_item_post(response):
    """
    Add data to response   from steem and Ethereum blockchain
    """
    logging.debug('after_fetch_item_post')
    logging.debug(response)
    if  response['state'] in ['steemed', 'Success',]:
        steem_post = client.get_content(response['steemauthor'], response['steempermlink'])
        logging.debug(steem_post)
        #Replace in response some fields with actual from steem
        response['steemtitle'] = steem_post['title']
        response['steembody']  = steem_post['body']
        r =web3tool.get_data_from_receipt(
            response['blockchainplus'][-1:][0]['txHash']
        )
        response['blockchainplus'][-1:][0]['savedEthereumtHash'] = r[1]
        response['blockchainplus'][-1:][0]['calculatedPostHash'] = web3tool.calc_hash(
            steem_post['title'],
            steem_post['body']
        )
        response['blockchainplus'][-1:][0]['FromSteemUrl'] = web3tool.get_sha3(steem_post['url'])
        response['blockchainplus'][-1:][0]['SavedPostUrl'] = r[0]
        response['blockchainplus'][-1:][0]['txExplorerLink'] = (settings.WEB3_EXPLORER_TX_BASE
            + response['blockchainplus'][-1:][0]['txHash'])
    
###########################################################################
###########################################################################
###########################################################################
#Steem initializing   (read only, no keys needed)
client = steem.Steem(no_broadcassteemtitlet=False,
    #keys=[settings.STEEM_POSTING_PK , settings.STEEM_ACTIVE_PK]
)

if  __name__ == '__main__':
    logging.debug('****env** '+settings.STEEM_TAG,)
    #r = client.get_content(settings.STEEM_SYNPAT_AUTHOR, settings.STEEM_TAG)
    r = client.get_discussions_by_created(
        {"tag":settings.STEEM_TAG,
         "limit":100, #number of posts
       #Below presents in steem docs, but not  work
       #https://github.com/steemit/steem/issues/1233
    # "filter_tags": [],
    # "select_authors": [],
    # "select_tags": [],
#     #  "truncate_body": 0
        }
    )
    logging.debug(r)