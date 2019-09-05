import numpy as np 
import matplotlib.pyplot as plt 

class Bandit:
    def __init__(self, m, upper_limit = 0):
        self.m = m 
        self.mean = upper_limit
        self.N = 0
    
    def pull(self):
        return np.random.randn() + self.m #reward given by pulling this band
    
    def update(self, x):
        self.N += 1
        self.mean = (1.0 - 1.0/self.N)*self.mean + 1.0/self.N*x

def run_experiment_optimistic_initial_value():
    
    bandits_opt_value = [Bandit(m1, 10), Bandit(m2, 10), Bandit(m3, 10)]
    data_opt_value = np.empty(N)

    for i in range(N):
        #optimistic initial value
        j_op = np.argmax([b.mean for b in bandits_opt_value])
        x_opt_val = bandits_opt_value[j_op].pull()
        bandits_opt_value[j_op].update(x_opt_val)

        #for the plot
        data_opt_value[i] = x_opt_val
    
    cumulative_average = np.cumsum(data) / (np.arange(N) + 1)
    cumulative_average_opt_value = np.cumsum(data_opt_value) / (np.arange(N) + 1)
    
    # plot moving average ctr 
    plt.plot(cumulative_average_opt_value, label = 'Optimistic Value')
    plt.plot(np.ones(N)*m1)
    plt.plot(np.ones(N)*m2)
    plt.plot(np.ones(N)*m3)
    plt.legend()
    plt.xscale('log')
    plt.show()

    for b in bandits_opt_value:
        print(b.mean)
    
    return cumulative_average_opt_value

def run_experiment(m1, m2, m3, eps, N):
    bandits = [Bandit(m1), Bandit(m2), Bandit(m3)]
    bandits_opt_value = [Bandit(m1, 10), Bandit(m2, 10), Bandit(m3, 10)]
    data = np.empty(N)
    data_opt_value = np.empty(N)

    for i in range(N):
        #epsilon greedy
        p = np.random.random()
        if p < eps:
            j = np.random.choice(3)
        else:
            j = np.argmax([b.mean for b in bandits])
        x = bandits[j].pull()
        bandits[j].update(x)

        #optimistic initial value
        j_op = np.argmax([b.mean for b in bandits_opt_value])
        x_opt_val = bandits_opt_value[j_op].pull()
        bandits_opt_value[j_op].update(x_opt_val)

        # for the plot
        data[i] = x
        data_opt_value[i] = x_opt_val
    
    cumulative_average = np.cumsum(data) / (np.arange(N) + 1)
    cumulative_average_opt_value = np.cumsum(data_opt_value) / (np.arange(N) + 1)
    
    # plot moving average ctr 
    plt.plot(cumulative_average, label = 'Epsilon Greedy')
    plt.plot(cumulative_average_opt_value, label = 'Optimistic Value')
    plt.plot(np.ones(N)*m1)
    plt.plot(np.ones(N)*m2)
    plt.plot(np.ones(N)*m3)
    plt.legend()
    plt.xscale('log')
    plt.show()

    for b in bandits:
        print(b.mean)

    for b in bandits_opt_value:
        print(b.mean)
    
    return [cumulative_average, cumulative_average_opt_value]

if __name__ == "__main__":
    c_1 = run_experiment(1.0, 2.0, 3.0, 0.1, 100000)
    c_05 = run_experiment(1.0, 2.0, 3.0, 0.05, 100000)
    c_01 = run_experiment(1.0, 2.0, 3.0, 0.01, 100000)

    # log scale plot
    plt.plot(c_1[0], label='eps = 0.1')
    plt.plot(c_1[1], label='O.V eps = 0.1')
    plt.plot(c_05[0], label='eps = 0.05')
    plt.plot(c_05[1], label='O.V eps = 0.05')
    plt.plot(c_01[0], label='eps = 0.01')
    plt.plot(c_01[1], label='O.V eps = 0.01')
    plt.legend()
    plt.xscale('log')
    plt.show()

    # linear plot
    plt.plot(c_1[0], label='eps = 0.1')
    plt.plot(c_1[1], label='O.V eps = 0.1')
    plt.plot(c_05[0], label='eps = 0.05')
    plt.plot(c_05[1], label='O.V eps = 0.05')
    plt.plot(c_01[0], label='eps = 0.01')
    plt.plot(c_01[1], label='O.V eps = 0.01')
    plt.legend()
    plt.show()