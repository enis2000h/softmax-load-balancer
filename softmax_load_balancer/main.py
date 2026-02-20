from simulation import run_simulation
from metrics import average_latency, total_reward

latencies, rewards = run_simulation()

print("Average latency:", average_latency(latencies))
print("Total reward:", total_reward(rewards))
