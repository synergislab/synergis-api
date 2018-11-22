## Synergis API


### Synpat service API
Synpat service API expose one endpoint: **posts**. It  represent Steem posts 
collection that store in Synpat service database. This database is buffer
 temporary storage just for convenience. All records inserted in posts collection
  will written in Steem blockchain under *synpat* tag (additional tags are 
  possible ). After that you can read your post at https://steemit.com at full *url*
    `/synpat/@synpatauthor/now-we-can-save-our-ideas`. Then this full _url_ (plus Sha256 hash of _post title + post body_) will save in Ethereum blockchain at special
    Synpat service smart contract.  

In this document we use [httpie](https://httpie.org/) command line HTTP 
client for API method calls.

#### Create Steem post
Two params are required: **steembody**  and **steemtitle**
```bash
http -v http://ec2-52-53-197-230.us-west-1.compute.amazonaws.com:5000/synapi/V1/posts/ steemtitle='All we need is Steem and Ethereum' steembody='Если Вы произвели оплату, перейдите пожалуйста в ТайПад https://btllab.timepad.ru/event/832583/ где проходили регистрацию, там есть кнопка вернуть билет. Деньги Вам будут возвращены в полном объеме. .' steemtags:='["timepad","eticket", "wish"]'

#Http Request
POST /synapi/V1/posts/ HTTP/1.1
Accept: application/json, */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Content-Length: 973
Content-Type: application/json
Host: ec2-52-53-197-230.us-west-1.compute.amazonaws.com:5000
User-Agent: HTTPie/1.0.0

{
    "steembody": "Если Вы произвели оплату, перейдите пожалуйста в ТайПад https://btllab.timepad.ru/event/832583/ где проходили регистрацию, там есть кнопка вернуть билет. Деньги Вам будут возвращены в полном объеме. .",
    "steemtags": [
        "timepad",
        "eticket",
        "wish"
    ],
    "steemtitle": "All we need is Steem and Ethereum"
}

#HTTP Response
HTTP/1.0 201 CREATED
Content-Length: 276
Content-Type: application/json
Date: Thu, 22 Nov 2018 07:54:33 GMT
Location: http://ec2-52-53-197-230.us-west-1.compute.amazonaws.com:5000/posts/5bf660b91859a0001a0abe9f
Server: Eve/0.8.1 Werkzeug/0.14.1 Python/3.7.1

{
    "_created": "Thu, 22 Nov 2018 07:54:33 GMT",
    "_etag": "1d8805605f1c094211fdf619e135396bd474d069",
    "_id": "5bf660b91859a0001a0abe9f",
    "_links": {
        "self": {
            "href": "posts/5bf660b91859a0001a0abe9f",
            "title": "Post"
        }
    },
    "_status": "OK",
    "_updated": "Thu, 22 Nov 2018 07:54:33 GMT"
}

```

#### Get Steem post by synpat database id
All response fields which names start with "\_" are service fields.  
Other fields explanation you can find below call example
```bash
http -v http://ec2-52-53-197-230.us-west-1.compute.amazonaws.com:5000/synapi/V1/posts/5bf660b91859a0001a0abe9f

#HTTP Request
GET /synapi/V1/posts/5bf660b91859a0001a0abe9f HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: ec2-52-53-197-230.us-west-1.compute.amazonaws.com:5000
User-Agent: HTTPie/1.0.0


#HTTP Response
HTTP/1.0 200 OK
Content-Length: 1982
Content-Type: application/json
Date: Thu, 22 Nov 2018 08:01:52 GMT
ETag: "1d8805605f1c094211fdf619e135396bd474d069"
Last-Modified: Thu, 22 Nov 2018 07:54:33 GMT
Server: Eve/0.8.1 Werkzeug/0.14.1 Python/3.7.1

{
    "_created": "Thu, 22 Nov 2018 07:54:33 GMT",
    "_etag": "1d8805605f1c094211fdf619e135396bd474d069",
    "_id": "5bf660b91859a0001a0abe9f",
    "_links": {
        "collection": {
            "href": "posts",
            "title": "posts"
        },
        "parent": {
            "href": "/",
            "title": "home"
        },
        "self": {
            "href": "posts/5bf660b91859a0001a0abe9f",
            "title": "Post"
        }
    },
    "_updated": "Thu, 22 Nov 2018 07:54:33 GMT",
    "blockchainplus": [
        {
            "FromSteemUrl": "0x7651d93e3bbb0d438ca75cdc4196f482c34bda9e8f0c54ee551a579671b0d2d5",
            "SavedPostUrl": "0x7651d93e3bbb0d438ca75cdc4196f482c34bda9e8f0c54ee551a579671b0d2d5",
            "blockNumber": 3382980,
            "calculatedPostHash": "0x50cec02243ffd2104012f7523f68899951b5dfb588bf7b7fa9d6b7ac2d85fd91",
            "savedEthereumtHash": "0x50cec02243ffd2104012f7523f68899951b5dfb588bf7b7fa9d6b7ac2d85fd91",
             "txExplorerLink": "https://rinkeby.etherscan.io/tx/0x9fa177b0af7e9209ada37ab1caef76fc525256340422a3a876f261686d0b9580",
            "txHash": "0x9fa177b0af7e9209ada37ab1caef76fc525256340422a3a876f261686d0b9580"
        }
    ],
    "ethaddr": "0xafB42ffDC859f82eDb3E93680F95212200f0CCA1",
    "state": "Success",
    "steemauthor": "maxsiz",
    "steembody": "Если Вы произвели оплату, перейдите пожалуйста в ТайПад https://btllab.timepad.ru/event/832583/ где проходили регистрацию, там есть кнопка вернуть билет. Деньги Вам будут возвращены в полном объеме. .",
    "steempermlink": "all-we-need-is-steem-and-ethereum",
    "steemtags": [
        "timepad",
        "eticket",
        "wish"
    ],
    "steemtitle": "All we need is Steem and Ethereum",
    "txForSign": null
}
```

* __ethaddr__ - Ethereum address from which Ethereum transaction was executed. Default
value is synpat service address (see source).  
* __state__ - current state of post proccessing. It can be one of following: "new", 
"steemed", "readyForSign", "ethSigned", "ethPending", "Success", "Failure", "error".
* __steemauthor__ - Steem account name, default value is _synpat_.
* __steemtitle__ - Steem post title, not more than 255 characters.
* __steembody__ - Steem post body, not more than 64K
* __steempermlink__ - Steem url last element. Must be unique for author. 
* __steemtags__ - Steem tags list. At https://steemit.com you can obtain not more than
4 tags but you can use more. First tag is always "synpat".  
* __txForSign__ - [Ethereum transaction object](https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_sendtransaction). This field is not null  for record in "readyForSign" 
state. It can be used for sign with https://www.myetherwallet.com/  or 
other third side tools.
* __blockchainplus__  - quintessence object of synpat service (list of objects). All of its fields(except __txHash__) are calculate or request directly from blockchain (Steem or Ethereum). When this API method (i.e for item) is called __synpat__ service query Steem blockchain post by _author_=@synpat and _permlink_= permlink. The response contains full 
steem post information. 
  * __FromSteemUrl__ - result [Keccak SHA256](https://web3py.readthedocs.io/en/latest/overview.html#cryptographic-hashing) of _/steem_category/@steem_author/steem-permlink_, unique post's identifier (@steem_author + steem-permlink). For _synpat service_ posts it always **synpat**. It is "url" field of full steem post object.
  * __SavedPostUrl__ - same as __FromSteemUrl__, but from Ethereum blockchain transaction. It was stored there during post creation. If  __SavedPostUrl__ == __FromSteemUrl__ then synpat refers to correct transaction in Ethereum.  
  * __calculatedPostHash__ - synpat service concatenate title an body from full steem post object and calculate for it [Sha3 Solidity style hash](https://web3py.readthedocs.io/en/latest/overview.html#Web3.soliditySha3).
  * __savedEthereumtHash__ - same as __calculatedPostHash__, but Ethereum blockchain transaction. It was stored there during post creation. If __savedEthereumtHash__ == __calculatedPostHash__ then steem post title and body are have not changed since creation.
  * __blockNumber__ - Ethereum blockchain block number in which transaction (__txHash__) was included. So post creation time is not later than this block time creation.
  * __txHash__ - transaction hash. 
  * __txExplorerLink__ - convenient blockchain explorer link to __txHash__ transaction.


#### Get Steem post by Steem permalink
```bash
http -v http://ec2-52-53-197-230.us-west-1.compute.amazonaws.com:5000/synapi/V1/posts/all-we-need-is-steem-and-ethereum

#HTTP Request
GET /synapi/V1/posts/all-we-need-is-steem-and-ethereum HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: ec2-52-53-197-230.us-west-1.compute.amazonaws.com:5000
User-Agent: HTTPie/1.0.0


#HTTP Response
HTTP/1.0 200 OK
Content-Length: 1982
Content-Type: application/json
Date: Thu, 22 Nov 2018 08:05:13 GMT
ETag: "1d8805605f1c094211fdf619e135396bd474d069"
Last-Modified: Thu, 22 Nov 2018 07:54:33 GMT
Server: Eve/0.8.1 Werkzeug/0.14.1 Python/3.7.1

{
    "_created": "Thu, 22 Nov 2018 07:54:33 GMT",
    "_etag": "1d8805605f1c094211fdf619e135396bd474d069",
    "_id": "5bf660b91859a0001a0abe9f",
    "_links": {
        "collection": {
            "href": "posts",
            "title": "posts"
        },
        "parent": {
            "href": "/",
            "title": "home"
        },
        "self": {
            "href": "posts/5bf660b91859a0001a0abe9f",
            "title": "Post"
        }
    },
    "_updated": "Thu, 22 Nov 2018 07:54:33 GMT",
    "blockchainplus": [
        {
            "FromSteemUrl": "0x7651d93e3bbb0d438ca75cdc4196f482c34bda9e8f0c54ee551a579671b0d2d5",
            "SavedPostUrl": "0x7651d93e3bbb0d438ca75cdc4196f482c34bda9e8f0c54ee551a579671b0d2d5",
            "blockNumber": 3382980,
            "calculatedPostHash": "0x50cec02243ffd2104012f7523f68899951b5dfb588bf7b7fa9d6b7ac2d85fd91",
            "savedEthereumtHash": "0x50cec02243ffd2104012f7523f68899951b5dfb588bf7b7fa9d6b7ac2d85fd91",
             "txExplorerLink": "https://rinkeby.etherscan.io/tx/0x9fa177b0af7e9209ada37ab1caef76fc525256340422a3a876f261686d0b9580",
            "txHash": "0x9fa177b0af7e9209ada37ab1caef76fc525256340422a3a876f261686d0b9580"
        }
    ],
    "ethaddr": "0xafB42ffDC859f82eDb3E93680F95212200f0CCA1",
    "state": "Success",
    "steemauthor": "maxsiz",
    "steembody": "Если Вы произвели оплату, перейдите пожалуйста в ТайПад https://btllab.timepad.ru/event/832583/ где проходили регистрацию, там есть кнопка вернуть билет. Деньги Вам будут возвращены в полном объеме. .",
    "steempermlink": "all-we-need-is-steem-and-ethereum",
    "steemtags": [
        "timepad",
        "eticket",
        "wish"
    ],
    "steemtitle": "All we need is Steem and Ethereum",
    "txForSign": null
}

```

#### Get all Steem posts from synpat database
```bash
http -v http://ec2-52-53-197-230.us-west-1.compute.amazonaws.com:5000/synapi/V1/posts/

#HTTP Request
GET /synapi/V1/posts/ HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: ec2-52-53-197-230.us-west-1.compute.amazonaws.com:5000
User-Agent: HTTPie/1.0.0


#HTTP Response
HTTP/1.0 200 OK
Content-Length: 3231
Content-Type: application/json
Date: Thu, 22 Nov 2018 09:04:08 GMT
Last-Modified: Thu, 22 Nov 2018 07:54:33 GMT
Server: Eve/0.8.1 Werkzeug/0.14.1 Python/3.7.1
X-Total-Count: 2

{
    "_items": [
        {
            "_created": "Wed, 21 Nov 2018 17:44:11 GMT",
            "_etag": "94c8afe846a61662c88827a15eef788718de4d15",
            "_id": "5bf5996b1859a0001a0abe9e",
            "_links": {
                "self": {
                    "href": "posts/5bf5996b1859a0001a0abe9e",
                    "title": "Post"
                }
            },
            "_updated": "Wed, 21 Nov 2018 17:44:11 GMT",
            "blockchainplus": [
                {
                    "blockNumber": 3379598,
                    "txHash": "0xa2fe2a7fc27cdf64700e31261011b0da43f43101fe5f0ddee1ab386372616cc4"
                }
            ],
            "ethaddr": "0xafB42ffDC859f82eDb3E93680F95212200f0CCA1",
            "state": "Success",
            "steemauthor": "maxsiz",
            "steembody": "Если Вы произвели оплату, перейдите пожалуйста в ТаймПад https://btllab.timepad.ru/event/832583/ где проходили регистрацию, там есть кнопка вернуть билет. Деньги Вам будут возвращены в полном объеме. .",
            "steempermlink": "how-to-make-it-realy-fasttt",
            "steemtags": [
                "timepad",
                "eticket"
            ],
            "steemtitle": "How to make it realy fast. Realy FAST!",
            "txForSign": null
        },
        {
            "_created": "Thu, 22 Nov 2018 07:54:33 GMT",
            "_etag": "1d8805605f1c094211fdf619e135396bd474d069",
            "_id": "5bf660b91859a0001a0abe9f",
            "_links": {
                "self": {
                    "href": "posts/5bf660b91859a0001a0abe9f",
                    "title": "Post"
                }
            },
            "_updated": "Thu, 22 Nov 2018 07:54:33 GMT",
            "blockchainplus": [
                {
                    "blockNumber": 3382980,
                    "txHash": "0x9fa177b0af7e9209ada37ab1caef76fc525256340422a3a876f261686d0b9580"
                }
            ],
            "ethaddr": "0xafB42ffDC859f82eDb3E93680F95212200f0CCA1",
            "state": "Success",
            "steemauthor": "maxsiz",
            "steembody": "Если Вы произвели оплату, перейдите пожалуйста в ТайПад https://btllab.timepad.ru/event/832583/ где проходили регистрацию, там есть кнопка вернуть билет. Деньги Вам будут возвращены в полном объеме. .",
            "steempermlink": "all-we-need-is-steem-and-ethereum",
            "steemtags": [
                "timepad",
                "eticket",
                "wish"
            ],
            "steemtitle": "All we need is Steem and Ethereum",
            "txForSign": null
        }
    ],
    "_links": {
        "parent": {
            "href": "/",
            "title": "home"
        },
        "self": {
            "href": "posts",
            "title": "posts"
        }
    },
    "_meta": {
        "max_results": 25,
        "page": 1,
        "total": 2
    }
}
```

#### Get Steem post by filter:  one  tag
```bash
http -v http://ec2-52-53-197-230.us-west-1.compute.amazonaws.com:5000/synapi/V1/posts/?where='{"steemtags":"wish"}'

#HTTP Request
GET /synapi/V1/posts/?where=%7B%22steemtags%22:%22wish%22%7D HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: ec2-52-53-197-230.us-west-1.compute.amazonaws.com:5000
User-Agent: HTTPie/1.0.0


#HTTP Response
HTTP/1.0 200 OK
Content-Length: 1730
Content-Type: application/json
Date: Thu, 22 Nov 2018 09:22:18 GMT
Last-Modified: Thu, 22 Nov 2018 07:54:33 GMT
Server: Eve/0.8.1 Werkzeug/0.14.1 Python/3.7.1
X-Total-Count: 1

{
    "_items": [
        {
            "_created": "Thu, 22 Nov 2018 07:54:33 GMT",
            "_etag": "1d8805605f1c094211fdf619e135396bd474d069",
            "_id": "5bf660b91859a0001a0abe9f",
            "_links": {
                "self": {
                    "href": "posts/5bf660b91859a0001a0abe9f",
                    "title": "Post"
                }
            },
            "_updated": "Thu, 22 Nov 2018 07:54:33 GMT",
            "blockchainplus": [
                {
                    "blockNumber": 3382980,
                    "txHash": "0x9fa177b0af7e9209ada37ab1caef76fc525256340422a3a876f261686d0b9580"
                }
            ],
            "ethaddr": "0xafB42ffDC859f82eDb3E93680F95212200f0CCA1",
            "state": "Success",
            "steemauthor": "maxsiz",
            "steembody": "Если Вы произвели оплату, перейдите пожалуйста в ТайПад https://btllab.timepad.ru/event/832583/ где проходили регистрацию, там есть кнопка вернуть билет. Деньги Вам будут возвращены в полном объеме. .",
            "steempermlink": "all-we-need-is-steem-and-ethereum",
            "steemtags": [
                "timepad",
                "eticket",
                "wish"
            ],
            "steemtitle": "All we need is Steem and Ethereum",
            "txForSign": null
        }
    ],
    "_links": {
        "parent": {
            "href": "/",
            "title": "home"
        },
        "self": {
            "href": "posts?where={\"steemtags\":\"wish\"}",
            "title": "posts"
        }
    },
    "_meta": {
        "max_results": 25,
        "page": 1,
        "total": 1
    }
}
```

#### Get Steem posts by filter:  two  tags
```bash
http -v http://ec2-52-53-197-230.us-west-1.compute.amazonaws.com:5000/synapi/V1/posts/?where='{"steemtags":"wish","steemtags":"idea"}'

#HTTP Request
GET /synapi/V1/posts/?where=%7B%22steemtags%22:%22wish%22,%22steemtags%22:%22idea%22%7D HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: ec2-52-53-197-230.us-west-1.compute.amazonaws.com:5000
User-Agent: HTTPie/1.0.0


#HTTP Response
HTTP/1.0 200 OK
Content-Length: 1095
Content-Type: application/json
Date: Thu, 22 Nov 2018 09:34:40 GMT
Last-Modified: Thu, 22 Nov 2018 09:32:37 GMT
Server: Eve/0.8.1 Werkzeug/0.14.1 Python/3.7.1
X-Total-Count: 1

{
    "_items": [
        {
            "_created": "Thu, 22 Nov 2018 09:32:37 GMT",
            "_etag": "eb61aae018a37c7859933f80e06e97d2d62070b5",
            "_id": "5bf677b5e0999a001abfb9eb",
            "_links": {
                "self": {
                    "href": "posts/5bf677b5e0999a001abfb9eb",
                    "title": "Post"
                }
            },
            "_updated": "Thu, 22 Nov 2018 09:32:37 GMT",
            "blockchainplus": [
                {
                    "blockNumber": 3383371,
                    "txHash": "0x4720832d21de13def439b87b31c06e4c8cdb3680d8239ff935e02fe99e18a893"
                }
            ],
            "ethaddr": "0xafB42ffDC859f82eDb3E93680F95212200f0CCA1",
            "state": "Success",
            "steemauthor": "maxsiz",
            "steembody": "Деньги Вам будут возвращены в полном объеме. .",
            "steempermlink": "now-we-can-save-our-ideas",
            "steemtags": [
                "idea",
                "wish"
            ],
            "steemtitle": "Now we can save our ideas?",
            "txForSign": null
        }
    ],
    "_links": {
        "parent": {
            "href": "/",
            "title": "home"
        },
        "self": {
            "href": "posts?where={\"steemtags\":\"wish\",\"steemtags\":\"idea\"}",
            "title": "posts"
        }
    },
    "_meta": {
        "max_results": 25,
        "page": 1,
        "total": 1
    }
}
```

#### Get all Steem posts, specific fields
```bash
http -v http://ec2-52-53-197-230.us-west-1.compute.amazonaws.com:5000/synapi/V1/posts/?projection='{"steemtitle": 1, "steempermlink": 1}'

#HTTP Request
GET /synapi/V1/posts/?projection=%7B%22steemtitle%22:%201,%20%22steempermlink%22:%201%7D HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: ec2-52-53-197-230.us-west-1.compute.amazonaws.com:5000
User-Agent: HTTPie/1.0.0


#HTTP Response
HTTP/1.0 200 OK
Content-Length: 1246
Content-Type: application/json
Date: Thu, 22 Nov 2018 10:01:08 GMT
Last-Modified: Thu, 22 Nov 2018 09:32:37 GMT
Server: Eve/0.8.1 Werkzeug/0.14.1 Python/3.7.1
X-Total-Count: 3

{
    "_items": [
        {
            "_created": "Wed, 21 Nov 2018 17:44:11 GMT",
            "_etag": "94c8afe846a61662c88827a15eef788718de4d15",
            "_id": "5bf5996b1859a0001a0abe9e",
            "_links": {
                "self": {
                    "href": "posts/5bf5996b1859a0001a0abe9e",
                    "title": "Post"
                }
            },
            "_updated": "Wed, 21 Nov 2018 17:44:11 GMT",
            "steempermlink": "how-to-make-it-realy-fasttt",
            "steemtitle": "How to make it realy fast. Realy FAST!"
        },
        {
            "_created": "Thu, 22 Nov 2018 07:54:33 GMT",
            "_etag": "1d8805605f1c094211fdf619e135396bd474d069",
            "_id": "5bf660b91859a0001a0abe9f",
            "_links": {
                "self": {
                    "href": "posts/5bf660b91859a0001a0abe9f",
                    "title": "Post"
                }
            },
            "_updated": "Thu, 22 Nov 2018 07:54:33 GMT",
            "steempermlink": "all-we-need-is-steem-and-ethereum",
            "steemtitle": "All we need is Steem and Ethereum"
        },
        {
            "_created": "Thu, 22 Nov 2018 09:32:37 GMT",
            "_etag": "eb61aae018a37c7859933f80e06e97d2d62070b5",
            "_id": "5bf677b5e0999a001abfb9eb",
            "_links": {
                "self": {
                    "href": "posts/5bf677b5e0999a001abfb9eb",
                    "title": "Post"
                }
            },
            "_updated": "Thu, 22 Nov 2018 09:32:37 GMT",
            "steempermlink": "now-we-can-save-our-ideas",
            "steemtitle": "Now we can save our ideas?"
        }
    ],
    "_links": {
        "parent": {
            "href": "/",
            "title": "home"
        },
        "self": {
            "href": "posts",
            "title": "posts"
        }
    },
    "_meta": {
        "max_results": 25,
        "page": 1,
        "total": 3
    }
}
```
### Synbot API 
to be after..
