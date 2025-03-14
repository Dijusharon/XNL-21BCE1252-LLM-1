from web3 import Web3
infura_url = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
web3 = Web3(Web3.HTTPProvider(infura_url))

if web3.is_connected():
    print("✅ Successfully connected to Ethereum network")
else:
    print("❌ Connection to Ethereum failed!")
PRIVATE_KEY = "2704a5a01aff4cda8e8764c57f47862097df793394a3e80cc4ae88a60a4293be"
SENDER_ADDRESS = "0xA54D57b5750CDC367e20087D409EFbd6c5AC2f76"

def store_trade(transaction_id, trade_data):
    tx = {
        'from': SENDER_ADDRESS, 
        'to': '0xRecipientAddress',
        'value': web3.to_wei(0.01, 'ether'),
        'data': web3.to_hex(text=str(trade_data)), 
        'gas': 2000000,
        'gasPrice': web3.to_wei('50', 'gwei'),
        'nonce': web3.eth.get_transaction_count(SENDER_ADDRESS),  
    }

    
    signed_tx = web3.eth.account.sign_transaction(tx, private_key=PRIVATE_KEY)

    
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

    return tx_hash.hex()


if __name__ == "__main__":
    trade_data = {"symbol": "BTC", "price": 50000, "quantity": 0.5}
    print(store_trade("txn12345", trade_data))
