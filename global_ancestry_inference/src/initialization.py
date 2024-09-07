import numpy as np
from scipy.special import logsumexp

def simulated_annealing(test_data, P, num_populations, T_start=1.0, T_end=0.01, cooling_rate=0.995, max_iterations=1000):
    num_individuals = test_data.shape[0]
    Q = np.random.rand(num_individuals, num_populations)
    Q /= Q.sum(axis=1, keepdims=True)
    
    T = T_start
    
    for iteration in range(max_iterations):
        Q_new = Q + np.random.normal(0, 0.01, Q.shape)
        Q_new = np.clip(Q_new, 0, 1)
        Q_new /= Q_new.sum(axis=1, keepdims=True)
        
        log_likelihood_old = calculate_log_likelihood(test_data, P, Q)
        log_likelihood_new = calculate_log_likelihood(test_data, P, Q_new)
        
        if log_likelihood_new > log_likelihood_old or np.random.random() < np.exp((log_likelihood_new - log_likelihood_old) / T):
            Q = Q_new
        
        T *= cooling_rate
        if T < T_end:
            break
    
    return Q

def calculate_log_likelihood(test_data, P, Q):
    log_likelihood = 0
    for i in range(test_data.shape[0]):
        for l in range(test_data.shape[1]):
            p = np.sum(Q[i] * P[:, l])
            log_likelihood += test_data[i, l] * np.log(p) + (2 - test_data[i, l]) * np.log(1 - p)
    return log_likelihood