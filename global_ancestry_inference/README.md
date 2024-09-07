# Global Ancestry Inference Tool

This tool performs global ancestry inference using SNP data from individuals and a set of predefined ancestry populations.

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Method](#method)
5. [Input Data Format](#input-data-format)
6. [Output](#output)
7. [Testing](#testing)
8. [Dependencies](#dependencies)

## Introduction

The Global Ancestry Inference Tool is designed to estimate the ancestry proportions of individuals based on their SNP data and a set of reference populations. It uses a combination of simulated annealing for initialization and an Expectation-Maximization (EM) algorithm with scaling to account for unbalanced reference panels.

## Installation

1. Clone this repository:
git clone https://github.com/yourusername/global_ancestry_inference.git
cd global_ancestry_inference
2. Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
3. Install the required dependencies:
pip install -r requirements.txt
4. Install the package in editable mode:
pip install -e .
## Usage

Run the tool from the command line:
global_ancestry_inference --reference_file path/to/reference_data.csv --test_file path/to/test_data.csv --output_file path/to/results.csv --scaling_factor 1.0 --max_iterations 1000 --tolerance 1e-6
Arguments:
- `--reference_file`: Path to the reference population data file (required)
- `--test_file`: Path to the test individuals data file (required)
- `--output_file`: Path to save the output results (required)
- `--scaling_factor`: Scaling factor for population sizes (default: 1.0, range: 0-3)
- `--max_iterations`: Maximum number of EM iterations (default: 1000)
- `--tolerance`: Convergence tolerance for EM algorithm (default: 1e-6)

## Method

The tool uses the following steps to perform ancestry inference:

1. Data Loading: Load reference and test data from CSV files.
2. Allele Frequency Calculation: Calculate allele frequencies for each reference population.
3. Initialization: Use simulated annealing to generate an initial estimate of ancestry proportions (Q matrix).
4. EM Algorithm: Refine the Q matrix using an Expectation-Maximization algorithm with scaling to account for unbalanced reference panels.
5. Output: Save the final ancestry proportions and summary statistics.

### Key Equations

1. Expectation Step (E-step):
E[z_ila = k] = (q_ik * p_kl^x_ila * (1-p_kl)^(1-x_ila)) / Σ_m (q_im * p_ml^x_ila * (1-p_ml)^(1-x_ila))
where `z_ila` is the hidden variable indicating the source population of allele `a` at locus `l` for individual `i`.

2. Maximization Step (M-step):
q_ik = Σ_l Σ_a E[z_ila = k] / (2L)
where L is the number of loci.

3. Scaling:
q_ik_scaled = q_ik * (N_k)^s
where `N_k` is the size of population k and `s` is the scaling factor.

## Input Data Format

1. Reference File:
CSV file with columns: population, individual, snp1, snp2, ...

2. Test File:
CSV file with columns: individual, snp1, snp2, ...

SNP values should be coded as 0, 1, or 2, representing the number of minor alleles.

## Output

The tool produces a CSV file with the following columns:
- individual: Identifier for each test individual
- One column for each reference population, containing the ancestry proportion
- Max_Ancestry_Population: The population with the highest ancestry proportion
- Max_Ancestry_Proportion: The value of the highest ancestry proportion

## Testing

Run the tests using pytest:
pytest tests/
## Dependencies

- numpy (>= 1.21.0)
- pandas (>= 1.3.0)
- scipy (>= 1.7.0)
- pytest (>= 6.2.4) for testing

For a complete list of dependencies, see `requirements.txt`.