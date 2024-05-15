import csv

class Count_of_inferred_functions:
    def __init__(self, List_of_terms_file_path, Inferred_functions_file_path, OCG_clusters_file_path, GO_term, col_name):
        self.List_of_terms_file_path = List_of_terms_file_path
        self.Inferred_functions_file_path = Inferred_functions_file_path
        self.OCG_clusters_file_path = OCG_clusters_file_path
        self.GO_term = GO_term
        self.col_name = col_name

    def read_csv(self, file_path):
        data = []
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                data.append(row)
        return data

    def write_csv(self, data):
        with open(self.List_of_terms_file_path, 'w', newline='') as csvfile:
            fieldnames = data[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

    def count_GO_terms(self):
        comptage_data = self.read_csv(self.List_of_terms_file_path)
        class_data = self.read_csv(self.Inferred_functions_file_path)

        for comptage_row in comptage_data:
            search_term = comptage_row[self.GO_term]
            matching_class_ids = [row['ClassID'] for row in class_data if self.col_name in row and row[self.col_name] == search_term]


            with open(self.OCG_clusters_file_path, 'r') as textfile:
                lines = textfile.readlines()

            orf_proteins = set()
            for i, line in enumerate(lines):
                if line.startswith('>Class'):
                    class_id = line.split()[1]
                    if class_id in matching_class_ids:
                        j = i + 1
                        class_orfs = set()
                        while j < len(lines) and not lines[j].startswith('>'):
                            proteins = lines[j].split()
                            class_orfs.update([protein for protein in proteins if protein.startswith('ORF')])
                            j += 1
                        orf_proteins.update(class_orfs)

            total_orf_count = len(orf_proteins)
            comptage_row['Number_of_sPEP'] = total_orf_count

        self.write_csv(comptage_data)

# Use the class to count the number of general Go terms inferred to sPEPs
List_of_terms_file_path = '/home/slivak/Bureau/Interactome_sORF_monocytes/08_Analyse_inferred_functions/05_Output/comptage_nb_sPEP_fonctions_inferrees.csv'
Inferred_functions_file_path = '/home/slivak/Bureau/Interactome_sORF_monocytes/08_Analyse_inferred_functions/05_Output/HighQualityGraph.LargestComponent.partition.BP.cluster.with.one.or.more.sPEP.and.parent.term.csv'
OCG_clusters_file_path = '/home/slivak/Bureau/Interactome_sORF_monocytes/08_Analyse_inferred_functions/05_Output/OCG_clusters.txt'
GO_term = "Parent term"
col_name= "Parent.term"

go_counter_Parent_term = Count_of_inferred_functions(List_of_terms_file_path, Inferred_functions_file_path, OCG_clusters_file_path, GO_term, col_name)
go_counter_Parent_term.count_GO_terms()


#Use the class to count the exact number of GO terms inferred to sPEPs

List_of_terms_file_path = '/home/slivak/Bureau/Interactome_sORF_monocytes/08_Analyse_inferred_functions/05_Output/comptage_GO_exact_inferrés_aux_sPEPs.csv'
Inferred_functions_file_path = '/home/slivak/Bureau/Interactome_sORF_monocytes/08_Analyse_inferred_functions/05_Output/HighQualityGraph.LargestComponent.partition.BP.cluster.with.one.or.more.sPEP.and.parent.term.csv'
OCG_clusters_file_path = '/home/slivak/Bureau/Interactome_sORF_monocytes/08_Analyse_inferred_functions/05_Output/OCG_clusters.txt'
GO_term = "GO:BP"
col_name= "GoTermName"

go_counter_exact_term = Count_of_inferred_functions(List_of_terms_file_path, Inferred_functions_file_path, OCG_clusters_file_path, GO_term, col_name)
go_counter_exact_term.count_GO_terms()