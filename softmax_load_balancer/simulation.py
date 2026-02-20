from server import Server
from softmax_balancer import SoftmaxBalancer

def run_simulation(num_servers=3, steps=1000):
    servers = [Server(base_latency=50 + i * 10) for i in range(num_servers)]
    balancer = SoftmaxBalancer(num_servers)

    latencies = []
    rewards = []

    for _ in range(steps):
        idx = balancer.select_server()
        latency = servers[idx].get_latency()

        reward = 1 / latency
        balancer.update(idx, reward)

        latencies.append(latency)
        rewards.append(reward)

    return latencies, rewards
