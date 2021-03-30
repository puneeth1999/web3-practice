# Using abi and bytecode

import json
from web3 import Web3
from config import bytecode, app5_abi
####################Connection#######################

web3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
# print(web3.isConnected())

###################Setup#############################

web3.eth.defaultAccount = web3.eth.accounts[0]


abi = app5_abi
bytecode = bytecode

Greeter = web3.eth.contract(abi=abi, bytecode=bytecode)

tx_hash = Greeter.constructor().transact()


print(web3.toHex(tx_hash))


tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
print(tx_receipt)

contract = web3.eth.contract(
    address=tx_receipt.contractAddress,
    abi=abi
)

print(contract.functions.greet().call())
tx_hash = contract.functions.setGreeting('HEY THERE!').transact()
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
print(contract.functions.greet().call())
