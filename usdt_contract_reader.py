from web3 import Web3

rpc = "https://eth.llamarpc.com"
w3 = Web3(Web3.HTTPProvider(rpc))
USDT = "0xdAC17F958D2ee523a2206206994597c53D7087a11"

abi = [{"constant":True,"inputs":[{"name":"who","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"}]

def usdt_balance(address: str):
    contract = w3.eth.contract(address=USDT, abi=abi)
    bal = contract.functions.balanceOf(address).call()
    return bal / 1e6

if __name__ == "__main__":
    print(usdt_balance("0x1234567890123456789012345678901234567890"))
