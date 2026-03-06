
# REC Blockchain Fairness Experiment Environment

Includes:
- Hyperledger Fabric REC issuance
- Ethereum smart contract trading
- zk-SNARK fairness verification
- 100,000 transaction benchmark
- automated experiment scripts

Run:

docker compose up -d
python simulation/generate_dataset.py
python simulation/run_simulation.py
python benchmarks/scalability_test.py
