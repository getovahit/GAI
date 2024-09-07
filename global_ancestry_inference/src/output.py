import pandas as pd

def save_results(Q_final, populations, test_data, output_file):
    results_df = pd.DataFrame(Q_final, columns=populations)
    
    if isinstance(test_data, pd.DataFrame) and 'individual' in test_data.columns:
        results_df.insert(0, 'individual', test_data['individual'])
    else:
        results_df.insert(0, 'individual', [f'Individual_{i}' for i in range(len(Q_final))])
    
    max_ancestry = results_df.iloc[:, 1:].idxmax(axis=1)
    max_proportion = results_df.iloc[:, 1:].max(axis=1)
    results_df['Max_Ancestry_Population'] = max_ancestry
    results_df['Max_Ancestry_Proportion'] = max_proportion
    
    results_df.to_csv(output_file, index=False)
    print(f"Results saved to {output_file}")
    
    return results_df