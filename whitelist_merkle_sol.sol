// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract MerkleWhitelist {
    bytes32 public merkleRoot;

    constructor(bytes32 root) {
        merkleRoot = root;
    }

    function verify(bytes32[] calldata proof, address account) public view returns (bool) {
        bytes32 leaf = keccak256(abi.encodePacked(account));
        for (uint i; i < proof.length; i++) {
            if (leaf < proof[i]) {
                leaf = keccak256(abi.encodePacked(leaf, proof[i]));
            } else {
                leaf = keccak256(abi.encodePacked(proof[i], leaf));
            }
        }
        return leaf == merkleRoot;
    }
}
