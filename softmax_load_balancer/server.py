import numpy as np

class Server:
    def __init__(self, base_latency):
        self.base_latency = base_latency
        self.t = 0

    def get_latency(self):
        # non-stationary drift
        drift = 20 * np.sin(0.01 * self.t)

        # noise
        noise = np.random.normal(0, 5)

        self.t += 1
        latency = self.base_latency + drift + noise
        return max(latency, 1.0)
