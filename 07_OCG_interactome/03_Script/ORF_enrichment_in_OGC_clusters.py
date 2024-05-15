from scipy.stats import hypergeom
from statsmodels.stats.multitest import multipletests

# Constants
M = 11419  # Total number of IDs
n = 1816   # Total number of ORF IDs

# Function to calculate p-value for ORF enrichment
def calculate_p_value(N, x):
    p_value = hypergeom.sf(x-1, M, n, N)
    return p_value

# Function to read the file and process each cluster
def process_clusters(file_path, output_file):
    p_values = []
    class_numbers = []  # Store class numbers to ensure alignment with adjusted p-values
    N_values = []  # Store N values for each cluster
    x_values = []  # Store x values for each cluster
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('>Class'):
                # Extract class number from the line
                class_number = line.split()[1]
                class_numbers.append(class_number)
                # Try to extract number of nodes (N) from the line
                try:
                    N = int(''.join(filter(str.isdigit, line.split()[2])))
                    N_values.append(N)
                except ValueError:
                    print(f"Warning: Could not extract N from line: {line.strip()}")
                    continue  # Skip this line if N extraction fails
                # Read the next line to get IDs in the cluster
                ids_line = next(file).strip()
                # Count the number of IDs starting with 'ORF'
                x = sum(1 for id in ids_line.split() if id.startswith('ORF'))
                x_values.append(x)
                # Calculate p-value for ORF enrichment
                p_value = calculate_p_value(N, x)
                # Save the p-value for later adjustment
                p_values.append(p_value)

    # Adjust p-values using BH-FDR
    reject, adj_p_values, _, _ = multipletests(p_values, method='fdr_bh')

    # Write adjusted p-values to output file
    with open(output_file, 'w') as output:
        output.write("# Constants\n")
        output.write(f"M = {M}  # Total number of IDs\n")
        output.write(f"n = {n}   # Total number of ORF IDs\n\n")
        output.write("#p_values:\n")
        for class_number, N, x, p_value, adj_p_value in zip(class_numbers, N_values, x_values, p_values, adj_p_values):
            output.write(f"Cluster {class_number}: x = {x}, N = {N}, p-value = {p_value}, adj_p-value = {adj_p_value}\n")

# Example usage
file_path = '05_Output/OCG_clusters.txt'
output_file = '05_Output/Enrichment_sORF_in_clusters.txt'
process_clusters(file_path, output_file)
