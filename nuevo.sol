//SPDX-License-Identifier: MIT

pragma solidity >=0.7.0 <0.9.0;

contract nuevo {
    uint internal storedNumber;

    function getStoredNumber () public view returns(uint){
        return storedNumber;
    }

    function updateStoredNumber(uint newValue) public returns(uint){
        storedNumber = newValue;
        return storedNumber;
    }
}