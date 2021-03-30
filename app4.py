from web3 import Web3
import json
from config import app4_abi, app4_address
ganche_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganche_url))
address = web3.toChecksumAddress(app4_address)
abi = app4_abi

web3.eth.defaultAccount = web3.eth.accounts[0]
contract = web3.eth.contract(address=address, abi=abi)
tx_hash = contract.functions.setGreeting("Puneeth").transact()
# print(contract.functions.greet().call())

web3.eth.waitForTransactionReceipt(tx_hash)
print('Updated Greeting: {}'.format(
    contract.functions.greet().call()
))
print('The hash is:', web3.toHex(tx_hash))
