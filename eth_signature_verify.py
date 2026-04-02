from web3 import Web3
from eth_account.messages import encode_defunct

w3 = Web3()

def verify_eth_signature(message: str, signature: str, wallet_address: str):
    msg_encoded = encode_defunct(text=message)
    signer = w3.eth.account.recover_message(msg_encoded, signature=signature)
    is_valid = signer.lower() == wallet_address.lower()
    return {
        "message": message,
        "signature": signature,
        "wallet": wallet_address,
        "valid": is_valid,
        "recovered_address": signer
    }

if __name__ == "__main__":
    test_msg = "Login to Web3 DApp"
    test_sig = "0x..."  # 替换为真实签名
    test_addr = "0x..."
    print(verify_eth_signature(test_msg, test_sig, test_addr))
