def generate_hd_path(coin_type: int, index: int = 0):
    paths = {
        0: "m/44'/0'/0'/0/{}",    # BTC
        60: "m/44'/60'/0'/0/{}",  # ETH
        501: "m/44'/501'/0'/0/{}" # Solana
    }
    if coin_type not in paths:
        return "unsupported"
    return paths[coin_type].format(index)

if __name__ == "__main__":
    print("ETH:", generate_hd_path(60, 0))
    print("BTC:", generate_hd_path(0, 0))
    print("SOL:", generate_hd_path(501, 0))
