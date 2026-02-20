import numpy as np

def average_latency(latencies):
    return float(np.mean(latencies))

def total_reward(rewards):
    return float(np.sum(rewards))
