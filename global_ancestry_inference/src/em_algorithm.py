import numpy as np

def expectation_step(Q, P, test_data, scaling_factor, population_sizes):
    num_individuals, num_populations = Q.shape
    num_snps = P.shape[1]
    E = np.zeros((num_individuals, num_snps, 2, num_populations), dtype=np.float32)
    
    for i in range(num_individuals):
        for l in range(num_snps):
            for a in range(2):  # For each allele
                numerator = Q[i] * (P[:, l] if test_data[i, l] == a else (1 - P[:, l]))
                numerator *= np.power(population_sizes, scaling_factor)
                denominator = np.sum(numerator)
                E[i, l, a] = numerator / denominator
    
    return E

def maximization_step(E, test_data):
    num_individuals, num_populations = E.shape[0], E.shape[3]
    Q_new = np.zeros((num_individuals, num_populations), dtype=np.float32)
    
    for i in range(num_individuals):
        Q_new[i] = np.sum(E[i, :, :], axis=(0, 1)) / (2 * test_data.shape[1])
    
    return Q_new

def check_convergence(Q, Q_new, tolerance):
    return np.max(np.abs(Q - Q_new)) < tolerance

def run_em_algorithm(Q, P, test_data, population_sizes, scaling_factor, max_iterations=1000, tolerance=1e-6):
    for iteration in range(max_iterations):
        E = expectation_step(Q, P, test_data, scaling_factor, population_sizes)
        Q_new = maximization_step(E, test_data)
        
        if check_convergence(Q, Q_new, tolerance):
            print(f"EM algorithm converged after {iteration + 1} iterations.")
            return Q_new
        
        Q = Q_new
    
    print(f"EM algorithm did not converge after {max_iterations} iterations.")
    return Q