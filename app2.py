from web3 import Web3
import json
from config import infura_url, app2_abi, app3_address, app3_holder_address
web3 = Web3(Web3.HTTPProvider(infura_url))

# Check if the connection is established
print('Connection Established?:', web3.isConnected())

# JSON aray that describes what the smart contract looks like
abi = app2_abi
# Address of the smart contract. You can find it for any token on etheriumscan.io
address = app3_address

contract = web3.eth.contract(address=address, abi=abi)
print('contract:', contract)

# Total Supply
totalsupply = contract.functions.totalSupply().call()
totalsupply = web3.fromWei(totalsupply, 'ether')
print(totalsupply)

print(contract.functions.name().call())
print(contract.functions.symbol().call())

print(contract.functions.paused().call())
holder_address = app3_holder_address
holder_address = web3.toChecksumAddress(holder_address)
balance = contract.functions.balanceOf(holder_address).call()
balance = web3.fromWei(balance, 'ether')
print(balance)
