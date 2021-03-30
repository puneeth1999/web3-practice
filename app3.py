from web3 import Web3
from config import sender, receiver, sender_pvt_key
web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
# Installed ganache for dummy transactions


# We need the private key of the sender too

sender = sender
receiver = receiver
sender_pvt_key = sender_pvt_key


# Get the nance
nonce = web3.eth.getTransactionCount(sender)
print('Nonce of the sender:', nonce)
# Define the transaction
tx = {
    'nonce': nonce,
    'to': receiver,
    'value': web3.toWei(1, 'ether'),
    'gas': 200000,
    'gasPrice': web3.toWei(20, 'gwei')
}

# Sign the tx
signed_tx = web3.eth.account.signTransaction(tx, sender_pvt_key)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))  # toHex makes it more readable
