import numpy as np

def apply_scaling(Q, population_sizes, scaling_factor):
    return Q * np.power(population_sizes, scaling_factor)