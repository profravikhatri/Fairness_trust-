
pragma solidity ^0.8.20;
contract RECTrading {
 struct REC { address owner; uint energy; uint certificates; }
 mapping(uint=>REC) public recs; uint public recCount;
 function issueREC(uint energy) public {
  uint cert = energy * 80 / 100;
  recs[recCount] = REC(msg.sender, energy, cert);
  recCount++;
 }
 function tradeREC(uint id,address buyer) public {
  require(recs[id].owner == msg.sender);
  recs[id].owner = buyer;
 }
}
