def parse_evm_bytecode(bytecode: str):
    bytecode = bytecode.lower().removeprefix("0x")
    opcodes = []
    i = 0
    while i < len(bytecode):
        op = bytecode[i:i+2]
        opcodes.append(op)
        i += 2
    return {
        "length": len(bytecode) // 2,
        "opcodes": opcodes[:20],
        "has_deploy_code": "60806040" in bytecode
    }

if __name__ == "__main__":
    code = "0x608060405234801561001057600080fd5b50610150806100206000396000f3fe6080604052348015600f57600080fd5b506004361060325760003560e01c80632096525514603757806370a08231146062575b600080fd5b60606004803603810190605f9190602001906094565b607e6001600160a01b031916607e565b600055565b6000549056fea26469706673582212201a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b64736f6c634300081a0033"
    print(parse_evm_bytecode(code))
