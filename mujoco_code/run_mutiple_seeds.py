import subprocess
import sys

seeds = [1, 2, 3]

processes = []

for seed in seeds:
    cmd = [
        sys.executable,
        "DDPG.py",
        "--manual_seed",
        str(seed)
    ]
    p = subprocess.Popen(cmd)
    processes.append(p)

for p in processes:
    p.wait()

print("All experiments finished.")