from web3 import Web3
import time

w3 = Web3(Web3.HTTPProvider("https://eth.llamarpc.com"))

def gas_now():
    fee = w3.eth.fee_history(1, 'latest', [25, 50, 75])
    return {
        "baseFee": fee['baseFeePerGas'][-1] / 1e9,
        "priorityFee": [p/1e9 for p in fee['reward'][0]]
    }

if __name__ == "__main__":
    while True:
        print(gas_now())
        time.sleep(5)
