# -*- coding: utf-8 -*-
"""
All function  dependig on   web3.py - Ethereum
"""
import logging
import settings
from web3 import Web3, HTTPProvider, IPCProvider

#web3 provider initializing
if ('http:'.upper() in settings.WEB3_PROVIDER.upper() or
    'https:'.upper() in settings.WEB3_PROVIDER.upper()):
    w3 = Web3(HTTPProvider(settings.WEB3_PROVIDER))
elif ('ws:'.upper() in settings.WEB3_PROVIDER.upper() or
      'wss:'.upper() in settings.WEB3_PROVIDER.upper()):
    w3 = Web3(Web3.WebsocketProvider(settings.WEB3_PROVIDER))    
else:
    w3 = Web3(IPCProvider(settings.WEB3_PROVIDER))

# for quick  contract use
# synpatregister = w3.eth.contract(address=settings.ADDRESS_SYNPATREGISTER,
#     abi=settings.ABI_SYNPATREGISTER
# )
def get_data_from_receipt(_txHash):
    """
    Returns SynpatRecord event arguments (tuple) from tx receipt
    """
    r = w3.eth.getTransactionReceipt(_txHash)
    logging.debug('Tx Receipt')
    logging.debug(r)
    logging.debug('*********************************')
    #logging.debug(r['logs'][0]['topics'][1])
    #r2 = synpatregister.events.SynpatRecord().processReceipt(r)
    #logging.debug(r2)
    #return {'savedPostHash':r['logs'][0]['data']}
    logging.debug('data from receipt:')
    logging.debug('sha3 of url:')
    logging.debug(r['logs'][0]['topics'][1].hex())
    logging.debug('sha3 of title + body:')
    logging.debug(r['logs'][0]['data'])
    return (r['logs'][0]['topics'][1].hex(), r['logs'][0]['data'])


def calc_hash(_title, _body):
    """
    Returns solidity stile hash
    """
    r = w3.soliditySha3(
        ['string', 'string'], 
        [_title, _body]
    )
    logging.debug('Calculated soliditySha3')
    logging.debug(r.hex())
    return r.hex()


def get_sha3(_txt):
    """
    Returns keccak sha256 hash
    """
    return  Web3.sha3(text=_txt).hex()

if  __name__ == '__main__':
    pass