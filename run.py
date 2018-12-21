from eve import Eve
from settings import MONGO_URI
import os
import logging
import synsteem
#import settings
import pdf_download
app = Eve()
logging.basicConfig(format='%(asctime)s->%(levelname)s:[in %(filename)s:%(lineno)d]:%(message)s'
        , level=int(os.environ.get('EXO_LOGLEVEL',logging.DEBUG))
    )

# this wrapper is required to pass through app object to function
# that we can use app's db-connection
def pdf_download_wrapper(request, lookup):
	pdf_download.check_pdf(app, request, lookup)


###############################################################################
###############################################################################
###############################################
#                 Event Hooks                 #
###############################################

###########  Pre-Request Event Hooks ##########
#app.on_pre_POST_wallets += wallets.before_post
#app.on_pre_GET += balance_change_wrapper

###########  Post-Request Event Hooks ##########
#app.on_post_POST += balance_change_wrapper

###########   Database event hooks   ##########
#app.on_inserted_posts += wrapper_db_hook
#app.on_insert_wallets       += wallets.before_db_insert
app.on_fetched_item_posts += synsteem.after_fetch_item_post
app.on_pre_GET_orders += pdf_download_wrapper


if __name__ == '__main__':
    logging.info('****env**MONGODB_URI='+MONGO_URI)
    app.run(host='0.0.0.0')
