// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract Multicall {
    struct Call {
        address target;
        bytes data;
    }

    function multicall(Call[] calldata calls) external returns (bytes[] memory results) {
        results = new bytes[](calls.length);
        for (uint i; i < calls.length; i++) {
            (bool success, bytes memory ret) = calls[i].target.call(calls[i].data);
            require(success, "call failed");
            results[i] = ret;
        }
    }
}
