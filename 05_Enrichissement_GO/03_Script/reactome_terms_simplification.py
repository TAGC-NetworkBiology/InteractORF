import os
import pandas as pd
import csv

# Define the directory containing the files
directory = '/home/slivak/Bureau/Interactome_sORF_monocytes/05_Enrichissement_GO/01_Reference/gProfiler_results'

# Iterate over files in the directory
for filename in os.listdir(directory):
    # Check if the filename starts with 'gProfiler_hsapiens' and ends with '.csv'
    if filename.startswith('gProfiler_hsapiens') and filename.endswith('.csv'):
        # Extract the name part of the file
        file_name_part = filename.split('.')[0]
        # Construct the output filename
        output_filename = f"05_Output/Sipmified_REAC/simplified_REAC_{file_name_part}.csv"
        # Read the CSV file
        csv_file_path = os.path.join(directory, filename)
        df = pd.read_csv(csv_file_path, sep=',')
        # Filter rows where the 'source' column is 'REAC' and extract 'term_id' values
        reac_rows = df[df['source'] == 'REAC']
        reac_ids = reac_rows['term_id'].apply(lambda x: x.split(':')[1]).tolist()
        # Create dictionaries and process the data (as in the previous code snippet)
        child_to_parent = {}
        with open('/home/slivak/Bureau/Interactome_sORF_monocytes/05_Enrichissement_GO/01_Reference/ReactomePathwaysRelation.txt', 'r') as file:
            for line in file:
                parent_id, child_id = line.strip().split('\t')
                child_to_parent[child_id] = parent_id

        parent_descriptions = {}
        with open('/home/slivak/Bureau/Interactome_sORF_monocytes/05_Enrichissement_GO/01_Reference/ReactomePathways.txt', 'r') as file:
            for line in file:
                parts = line.strip().split('\t')
                parent_id = parts[0]
                description = parts[1] if len(parts) > 1 else ''
                parent_descriptions[parent_id] = description

        data = []
        for child_id in reac_ids:
            current_parent = child_to_parent.get(child_id)
            ultimate_parent = current_parent if current_parent else child_id  # Assign child_id if no parent available
            while current_parent in parent_descriptions:
                ultimate_parent = current_parent
                current_parent = child_to_parent.get(current_parent)
            description = parent_descriptions.get(ultimate_parent, '')
            data.append({'Child ID': child_id, 'Ultimate Parent ID': ultimate_parent, 'Description': description})

        # Create a DataFrame and save it to a CSV file with the constructed output filename
        df_result = pd.DataFrame(data)
        df_result.to_csv(output_filename, index=False)