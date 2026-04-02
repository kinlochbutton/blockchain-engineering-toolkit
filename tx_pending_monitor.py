from web3 import Web3
import threading
import time

w3 = Web3(Web3.HTTPProvider("https://eth.llamarpc.com"))

def monitor_pending():
    seen = set()
    while True:
        tx_hash = w3.eth.get_block_transaction_count('pending')
        if tx_hash not in seen:
            seen.add(tx_hash)
            print("Pending tx count:", tx_hash)
        time.sleep(2)

if __name__ == "__main__":
    threading.Thread(target=monitor_pending, daemon=True).start()
    input()
