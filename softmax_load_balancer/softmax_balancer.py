import numpy as np

class SoftmaxBalancer:
    def __init__(self, num_servers, tau=0.2, alpha=0.1):
        self.num_servers = num_servers
        self.tau = tau
        self.alpha = alpha
        self.q_values = np.zeros(num_servers)

    def select_server(self):
        prefs = self.q_values / self.tau

        # numerical stability: max çıkar
        m = np.max(prefs)
        exp_vals = np.exp(prefs - m)
        probs = exp_vals / np.sum(exp_vals)

        return np.random.choice(self.num_servers, p=probs)

    def update(self, server_index, reward):
        self.q_values[server_index] = (1 - self.alpha) * self.q_values[server_index] + self.alpha * reward
