'''import os
INFURA_PROJECT_ID = os.getenv("INFURA_PROJECT_ID")
infura_url = f"https://mainnet.infura.io/v3/46659c4d903b460db89f075a80c33fa2"
web3 = Web3(Web3.HTTPProvider(infura_url))'''


from web3 import Web3

infura_url = "https://mainnet.infura.io/v3/46659c4d903b460db89f075a80c33fa2"
web3 = Web3(Web3.HTTPProvider(infura_url))

if web3.is_connected():
    print("✅ Successfully connected to Ethereum via Infura!")
else:
    print("❌ Failed to connect to Infura.")
