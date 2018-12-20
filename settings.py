# -*- coding: utf-8 -*-

"""
    Synergis Lab 4T bot database API
    ~~~~~~~~~~~~~~~~~
    :license: BSD, see LICENSE for more details.
"""

import os
import json

##########################
##########################
## COMMON service settings
##########################
ENVIRON          = os.environ.get('ENVIRON','TEST')
#Some common params (secrets)
MONGO_URI        = os.environ.get('MONGODB_URI', 'mongodb://root:example@172.18.0.3/')
# MONGO_URI        = os.environ.get('MONGODB_URI', 'mongodb://172.18.0.3/')
WEB3_PROVIDER    = os.environ.get('WEB3_PROVIDER','wss://rinkeby.infura.io/ws/v3/22238a03c4ce4f6e9b2a3e0e899a77e6')
PK_OPERATOR      = os.environ.get('PK_OPERATOR','384D9719F2CDFA068A58811541AA1A6059306A4AE61A0A360EE6443D3F610977')
STEEM_POSTING_PK = os.environ.get('STEEM_POSTING_PK','5Kb1scKxP5cP4bujsPmL6z5YnRfEkMwWA1JidvV9DeddKRVPMhr')
STEEM_ACTIVE_PK  = os.environ.get('STEEM_ACTIVE_PK','5KWKj7TVQwnzk4awfAFEqfk9q54mUJDN8ycKLUqgCJREy6EZcTP')
# path to downloaded pdf storage
PATH_TO_PDF_STORAGE = os.environ.get('PATH_TO_PDF_STORAGE','.')

if  ENVIRON == 'TEST' :
    WEB3_NETWORK = 4
    WEB3_EXPLORER_TX_BASE = 'https://rinkeby.etherscan.io/tx/'
    #ADDRESS_SYNPATREGISTER = '0x128CB817Be464DE1df828FB1f44B4d28C7E7e1d8'
    ADDRESS_SYNPATREGISTER = '0xC40E4F272Cf6E37B28eeC0F3E0128e73C6627A80'
    ADDRESS_OPERATOR = '0xafB42ffDC859f82eDb3E93680F95212200f0CCA1'
    STEEM_TAG = 'testsynergis'
    STEEM_SYNPAT_AUTHOR = 'maxsiz'
else: #PROD settings
    WEB3_NETWORK = 1
    WEB3_EXPLORER_TX_BASE = 'https://etherscan.io/tx/'
    ADDRESS_SYNPATREGISTER = '0x2350b874D0EFf523c5847223eB7144e1E56f06cE'
    ADDRESS_OPERATOR = '0xDDA2F2E159d2Ce413Bd0e1dF5988Ee7A803432E3'
    STEEM_TAG = 'synpat'
    STEEM_SYNPAT_AUTHOR = 'menaskop'



# contracts ABI (!!!!! true->True, false ->False    - Python style)
ABI_SYNPATREGISTER = json.loads('[{"constant":true,"inputs":[{"name":"_hashinput","type":"string"}],"name":"calculateSha3","outputs":[{"name":"","type":"bytes32"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":false,"inputs":[],"name":"kill","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"bytes32"}],"name":"permlinkSaved","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"version","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_permlink","type":"string"},{"name":"_hashSha","type":"bytes32"}],"name":"writeSha3","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"pendingOwner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"payable":false,"stateMutability":"nonpayable","type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"permlinkSaved_permlink","type":"string"},{"indexed":false,"name":"_hashSha","type":"bytes32"}],"name":"SynpatRecord","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"previousOwner","type":"address"},{"indexed":true,"name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"}]')
##############################
## End of COMMON settings
##############################
##############################


# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST']

# Enable reads (GET), edits (PATCH) and deletes of individual items
# (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', ]

# We enable standard client cache directives for all resources exposed by the
# API. We can always override these global settings later.
# CACHE_CONTROL = 'max-age=20'
# CACHE_EXPIRES = 20
DEBUG = True
URL_PREFIX = 'synapi'
API_VERSION = 'V1'

#MONGO_URI = "mongodb://exo:exo123@ds141812.mlab.com:41812/settle"

###############################
### Synpat settings       #####
###############################
# SYNPAT_CONF = {
# 'SMARTCONTRACT' :'',
# 'STEEM_TAG'      : 'testsynergis',
# 'STEEM_SYNPAT_AUTHOR':'maxsiz',
# 'STEEM_POSTING_PK' :'5Kb1scKxP5cP4bujsPmL6z5YnRfEkMwWA1JidvV9DeddKRVPMhr',
# 'STEEM_ACTIVE_PK' :'5KWKj7TVQwnzk4awfAFEqfk9q54mUJDN8ycKLUqgCJREy6EZcTP'
# }
orders = {
     # 'title' tag used in item links.
    #'item_title': 'person',

    # by default the standard item entry point is defined as
    # '/orders/<ObjectId>/'. We leave it untouched, and we also enable an
    # additional read-only entry point. This way consumers can also perform GET
    # requests at '/orders/<project_name>/'.
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'project_name'
    },

     # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/pyeve/cerberus) for details.
    'schema':{
        'project_name':{
                'type': 'string',
                'minlength': 2,
                'maxlength': 50,
                'required' : True,
        },
        'project_site':{
                'type': 'string',
                'minlength': 2,
                'maxlength': 70,
                'required' : True,
        },
        'project_id':{
                'type': 'integer',
                'required' : True,
        },
        'descr':{
                'type': 'string',
                'maxlength' : 4000,
        },
        'entities':{
            'type': 'dict',
            'schema':{
                'wp':{
                    'type': 'dict',
                    'schema':{
                        'timestamp':{'type': 'integer'},
                        'data': {
                            'type': 'dict',
                            'schema':{
                                'parser_search' : {
                                    'type':'list',
                                    'schema':{
                                        'type':'dict',
                                        'schema': {
                                            'type': {'type': 'string', 'maxlength':12},
                                            'value': {'type': 'string','maxlength':250},
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                'team':{
                    'type': 'dict',
                    'schema':{
                        'timestamp':{'type': 'integer'},
                        'data': {
                            'type': 'dict',
                            'schema':{
                                'parser_search' : {
                                    'type':'list',
                                    'schema':{
                                        'type':'dict',
                                        'schema': {
                                            'type': {'type': 'string', 'maxlength':12},
                                            'value': {'type': 'string','maxlength':250},
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                'contact':{
                    'type': 'dict',
                    'schema':{
                        'timestamp':{'type': 'integer'},
                        'data': {
                            'type': 'dict',
                            'schema':{
                                'parser_search' : {
                                    'type':'list',
                                    'schema':{
                                        'type':'dict',
                                        'schema': {
                                            'type': {'type': 'string', 'maxlength':12},
                                            'value': {'type': 'string','maxlength':250},
                                            'downloaded': {
                                                'type': 'list',
                                                'schema':{
                                                    'filepath': {'type': 'string','maxlength':250},
                                                    'download_time': {'type': 'integer'},
                                                    'filehash': {'type': 'string','maxlength':50},
                                                }
                                            },
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                'repository':{
                    'type': 'dict',
                    'schema':{
                        'timestamp':{'type': 'integer'},
                        'data': {
                            'type': 'dict',
                            'schema':{
                                'parser_search' : {
                                    'type':'list',
                                    'schema':{
                                        'type':'dict',
                                        'schema': {
                                            'type': {'type': 'string', 'maxlength':12},
                                            'value': {'type': 'string','maxlength':250},
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                'news':{
                    'type': 'dict',
                    'schema':{
                        'timestamp':{'type': 'integer'},
                        'data': {
                            'type': 'dict',
                            'schema':{
                                'parser_search' : {
                                    'type':'list',
                                    'schema':{
                                        'type':'dict',
                                        'schema': {
                                            'type': {'type': 'string', 'maxlength':12},
                                            'value': {'type': 'string','maxlength':250},
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                'coin':{
                    'type': 'dict',
                    'schema':{
                        'timestamp':{'type': 'integer'},
                        'data': {
                            'type': 'dict',
                            'schema':{
                                'parser_search' : {
                                    'type':'list',
                                    'schema':{
                                        'type':'dict',
                                        'schema': {
                                            'type': {'type': 'string', 'maxlength':12},
                                            'value': {'type': 'string','maxlength':250},
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                'roadmap':{
                    'type': 'dict',
                    'schema':{
                        'timestamp':{'type': 'integer'},
                        'data': {
                            'type': 'dict',
                            'schema':{
                                'parser_search' : {
                                    'type':'list',
                                    'schema':{
                                        'type':'dict',
                                        'schema': {
                                            'type': {'type': 'string', 'maxlength':12},
                                            'value': {'type': 'boolean'},
                                        }
                                    }
                                }
                            }
                        }
                    }
                },

            }

        }

    }
}

posts = {
     # 'title' tag used in item links.
    #'item_title': 'person',

    # by default the standard item entry point is defined as
    # '/orders/<ObjectId>/'. We leave it untouched, and we also enable an
    # additional read-only entry point. This way consumers can also perform GET
    # requests at '/orders/<steempermlink>/'.
    'additional_lookup': {
        'url': 'regex("[\w-]+")',
        'field': 'steempermlink'
    },

    'schema':{
        'steemauthor':{
                'type': 'string',
                'minlength': 4,
                'maxlength': 70,
                'required' : True,
                'default': STEEM_SYNPAT_AUTHOR
        },
        'steemtitle':{
                'type': 'string',
                'minlength': 2,
                'maxlength': 255,
                'required' : True,
        },
        'steempermlink':{
                'type': 'string',
                'minlength': 2,
                'maxlength': 70,
        },


        'steembody':{
                'type': 'string',
                'minlength': 2,
                'maxlength': 65000,
                'required' : True,
        },

        'ethaddr':{
                'type': 'string',
                'minlength': 42,
                'maxlength': 42,
                'required' : True,
                'default'  : ADDRESS_OPERATOR
        },

        'steemtags':{
            'type'  : 'list',
            'schema': {
                'type'  : 'string',
                 'minlength': 2,
                 'maxlength': 25,
            }
        },

        'state':{
            'type': 'string',
            'allowed': ["new", "steemed"],
            'default':'new',
            'required' : True,
        },

        'txForSign':{
            'type': 'dict',
        },

        'blockchainplus':{
            'type':'list'
        }


    },
    'item_methods': ['GET']
}
# The DOMAIN dict explains which resources will be available and how they will
# be accessible to the API consumer.
DOMAIN = {
    'orders': orders,
    'posts': posts,
}

