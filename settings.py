# -*- coding: utf-8 -*-

"""
    Synergis Lab 4T bot database API
    ~~~~~~~~~~~~~~~~~
    :license: BSD, see LICENSE for more details.
"""

import os

# We want to seamlessy run our API both locally and on Heroku. If running on
# Heroku, sensible DB connection settings are stored in environment variables.
MONGO_URI = os.environ.get('MONGODB_URI', 'mongodb://exo:exo123@ds141812.mlab.com:41812/settle')


# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST']

# Enable reads (GET), edits (PATCH) and deletes of individual items
# (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'DELETE']

# We enable standard client cache directives for all resources exposed by the
# API. We can always override these global settings later.
CACHE_CONTROL = 'max-age=20'
CACHE_EXPIRES = 20
DEBUG = True


#MONGO_URI = "mongodb://exo:exo123@ds141812.mlab.com:41812/settle"

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


# The DOMAIN dict explains which resources will be available and how they will
# be accessible to the API consumer.
DOMAIN = {
    'orders': orders,
}

