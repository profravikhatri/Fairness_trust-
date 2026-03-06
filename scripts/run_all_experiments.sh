
#!/bin/bash
python simulation/generate_dataset.py
python simulation/run_simulation.py
python benchmarks/scalability_test.py
