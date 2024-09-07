import pandas as pd
import numpy as np

def load_reference_data(reference_file):
    df = pd.read_csv(reference_file)
    populations = df['population'].unique()
    num_populations = len(populations)
    num_snps = len(df.columns) - 2  # Subtract 'population' and 'individual' columns
    
    reference_data = [df[df['population'] == pop].iloc[:, 2:].values for pop in populations]
    
    return reference_data, num_populations, num_snps, populations

def load_test_data(test_file):
    df = pd.read_csv(test_file)
    num_individuals = len(df)
    num_snps = len(df.columns) - 1  # Subtract 'individual' column
    
    test_data = df.iloc[:, 1:].values
    
    return test_data, num_individuals, num_snps

def calculate_allele_frequencies(reference_data, num_populations, num_snps):
    P = np.zeros((num_populations, num_snps), dtype=np.float32)
    
    for k in range(num_populations):
        P[k] = np.sum(reference_data[k], axis=0) / (2 * len(reference_data[k]))
    
    return P