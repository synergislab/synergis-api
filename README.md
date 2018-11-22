## Synergis API


### Synpat service API
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

### Synbot API
