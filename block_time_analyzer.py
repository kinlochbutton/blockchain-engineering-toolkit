from web3 import Web3
import time

rpc = "https://eth.llamarpc.com"
w3 = Web3(Web3.HTTPProvider(rpc))

def block_speed(last_blocks=20):
    times = []
    latest = w3.eth.block_number
    for i in range(latest - last_blocks, latest):
        b1 = w3.eth.get_block(i)
        b2 = w3.eth.get_block(i+1)
        times.append(b2.timestamp - b1.timestamp)
    return {
        "avg_block_time": sum(times)/len(times),
        "max": max(times),
        "min": min(times),
        "samples": len(times)
    }

if __name__ == "__main__":
    print(block_speed())
