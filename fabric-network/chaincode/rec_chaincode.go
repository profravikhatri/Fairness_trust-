
package main
import (
 "encoding/json"
 "github.com/hyperledger/fabric-contract-api-go/contractapi"
)
type SmartContract struct { contractapi.Contract }
type REC struct { Owner string; Energy float64; Certificates float64 }
func (s *SmartContract) IssueREC(ctx contractapi.TransactionContextInterface, id string, energy float64) error {
 cert := energy * 0.8
 rec := REC{Owner: id, Energy: energy, Certificates: cert}
 recJSON, _ := json.Marshal(rec)
 return ctx.GetStub().PutState(id, recJSON)
}
func main() { chaincode,_:=contractapi.NewChaincode(new(SmartContract)); chaincode.Start() }
