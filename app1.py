from web3 import Web3
from config import infura_url, app1_account
web3 = Web3(Web3.HTTPProvider(infura_url))
print(web3.isConnected)
account = app1_account
balance = web3.eth.getBalance(
    account)
print('balance in Wei:', balance)
balance = web3.fromWei(balance, 'ether')
print('balance in Ether:', balance)
print(web3.eth.blockNumber)
