import argparse
from data_handling import load_reference_data, load_test_data, calculate_allele_frequencies
from initialization import simulated_annealing
from em_algorithm import run_em_algorithm
from output import save_results

def main(args):
    print("Loading reference data...")
    reference_data, num_populations, num_snps, populations = load_reference_data(args.reference_file)
    
    print("Calculating allele frequencies...")
    P = calculate_allele_frequencies(reference_data, num_populations, num_snps)
    
    print("Loading test data...")
    test_data, num_test_individuals, num_test_snps = load_test_data(args.test_file)
    
    if num_test_snps != num_snps:
        raise ValueError("Number of SNPs in test data doesn't match reference data")
    
    population_sizes = np.array([len(pop) for pop in reference_data])
    
    print("Running simulated annealing for initial Q estimate...")
    Q_initial = simulated_annealing(test_data, P, num_populations)
    
    print("Running EM algorithm with scaling...")
    Q_final = run_em_algorithm(Q_initial, P, test_data, population_sizes, args.scaling_factor, 
                               max_iterations=args.max_iterations, tolerance=args.tolerance)
    
    print("Saving results...")
    results_df = save_results(Q_final, populations, test_data, args.output_file)
    
    print("Analysis complete. Here's a summary of the results:")
    print(results_df[['individual', 'Max_Ancestry_Population', 'Max_Ancestry_Proportion']].head())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Global Ancestry Inference Tool")
    parser.add_argument("--reference_file", required=True, help="Path to the reference population data file")
    parser.add_argument("--test_file", required=True, help="Path to the test individuals data file")
    parser.add_argument("--output_file", required=True, help="Path to save the output results")
    parser.add_argument("--scaling_factor", type=float, default=1.0, help="Scaling factor for population sizes (0-3)")
    parser.add_argument("--max_iterations", type=int, default=1000, help="Maximum number of EM iterations")
    parser.add_argument("--tolerance", type=float, default=1e-6, help="Convergence tolerance for EM algorithm")
    
    args = parser.parse_args()
    main(args)