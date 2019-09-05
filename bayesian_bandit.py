import numpy as np 
import matplotlib.pyplot as plt 

class BayesianBandit:
    def __init__(self, true_mean):
        self.true_mean = true_mean
        #parameters for mu - prior is N(0, 1)
        self.predicted_mean = 0
        self.lambda_ = 1
        self.sum_x = 0 
        self.tau = 1

    def pull(self):
        return np.random.randn() + self.true_mean
    
    def sample(self):
        return np.random.randn() / np.sqrt(self.lambda_) + self.predicted_mean
    
    def update(self, x):
        self.lambda_ += self.tau
        self.sum_x = x
        self.predicted_mean = self.tau*self.sum_x / self.lambda_

def run_experiment(m1, m2, m3, N):
    bandits = [BayesianBandit(m1), BayesianBandit(m2), BayesianBandit(m3)]

    data = np.empty(N)

    for i in range(N):
        j = np.argmax([b.sample() for b in bandits])
        x = bandits[j].pull()
        bandits[j].update(x)

        data[i] = x 

    cumulative_average = np.cumsum(data) / (np.arange(N) + 1)

    # plot moving average ctr
    plt.plot(cumulative_average)
    plt.plot(np.ones(N)*m1)
    plt.plot(np.ones(N)*m2)
    plt.plot(np.ones(N)*m3)
    plt.xscale('log')
    plt.show()

    return cumulative_average

if __name__ == '__main__':
    m1 = 1.0
    m2 = 2.0
    m3 = 3.0

    bayes = run_experiment(m1, m2, m3, 100000)

    #log scale plot
    plt.plot(bayes, label='bayesian')
    plt.legend()
    plt.xscale('log')
    plt.show()
    
    #linear plot
    plt.plot(bayes, label='bayesian')
    plt.legend()
    plt.show()