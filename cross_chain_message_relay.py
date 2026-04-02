import hashlib
import json

class CrossChainRelay:
    def __init__(self, chain_id_from, chain_id_to):
        self.chain_from = chain_id_from
        self.chain_to = chain_id_to

    def sign_message(self, msg: dict, private_key: str):
        raw = json.dumps(msg, sort_keys=True) + private_key
        return hashlib.sha256(raw.encode()).hexdigest()

    def verify_relay(self, msg: dict, sig: str, public_key: str):
        expect = self.sign_message(msg, public_key)
        return expect == sig

if __name__ == "__main__":
    relay = CrossChainRelay(1, 5)  # ETH => Goerli
    msg = {"to": "0x123", "amt": 100}
    sig = relay.sign_message(msg, "pk")
    print(relay.verify_relay(msg, sig, "pk"))
