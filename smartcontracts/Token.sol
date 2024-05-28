pragma solidity ^0.8.0;

contract Token {
    
    string public name = "My Token";
    string public symbol = "MYT";
    uint256 public totalSupply = 1000000;
    mapping(address => uint256) public balanceOf;


    constructor() {
        balanceOf[msg.sender] = totalSupply;
    }

    function transfer(address _to, uint256 _value) public {
        require(balanceOf[msg.sender] >= _value);
        require(balanceOf[_to] + _value >= balanceOf[_to]);
        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;
    }

}