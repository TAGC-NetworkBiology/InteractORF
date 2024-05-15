from argparse import ArgumentParser

class Format_Data_cns():

    def __init__(self, file_path, output_path, algorithm, network): 
        self.file_path = file_path
        self.output_path = output_path
        self.algorithm = algorithm
        self.network = network
        self.multiculstered_node = self.read_multiclustered_nodes()
        self.formated_list = []
        self.create_class_dict()
        self.write_output_file()

    

    def read_multiclustered_nodes(self):    
        with open(self.file_path, "r") as fichier:
            # Lire toutes les lignes du fichier
            lignes = fichier.readlines()
            # Extraire la ligne 14 (index 13 car les indices commencent à 0)
            ligne_14 = lignes[13]
            # Supprimer les espaces et les parenthèses à la fin des identifiants
            prot_list = [prot.strip("(),") for prot in ligne_14.split()]
            identifiants = prot_list[::2]
        return identifiants

    def create_class_dict(self): 
        self.class_prot_dict = {}
        premier_signe = False
        with open(self.file_path, "r") as fichier:
            lignes = fichier.readlines()
            for idx, ligne in enumerate(lignes):
                if ligne.startswith('>'):
                    premier_signe = True
                    numéro_classe = ligne.split()
                    index_class = numéro_classe.index('>Class')
                    class_nombre = numéro_classe[index_class + 1]
                    nodes_nombre = int(numéro_classe[index_class + 2].strip('()'))
                    counter_multiclustered = 0 
                    list_prot_inside_class = [prot for prot in lignes[idx+1].split()]
                    for prot in list_prot_inside_class:
                        if prot in self.multiculstered_node: 
                            counter_multiclustered += 1 
                    self.formated_list.append(str(class_nombre) + "(" + str(nodes_nombre) + "," + str(counter_multiclustered) + ")") 
                    self.class_prot_dict[class_nombre] = list_prot_inside_class


    def write_output_file(self):
        with open(self.output_path, "w") as fichier:
            fichier.write("#ClustnSee analysis export\n")
            fichier.write("#Algorithm: {}\n".format(self.algorithm))  # Utilisation de la valeur spécifiée pour l'algorithme
            fichier.write("#Network: {}\n".format(self.network))  # Utilisation de la valeur spécifiée pour le réseau
            fichier.write("#Scope:Network\n")
            fichier.write("#Cluster Name (nb nodes in cluster, nb multi-classed nodes in cluster):\n")
            fichier.write(" ".join(self.formated_list))
            fichier.write("\n\n")
            # Écrire chaque classe et ses protéines
            for class_nombre, prot_list in self.class_prot_dict.items():
                fichier.write(">" + str(class_nombre) + "||\n")
                fichier.write("\n".join(prot_list))
                fichier.write("\n\n")

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--file_path", default='05_Output/OCG_clusters.txt')
    parser.add_argument("--output", default='05_Output/OCG_clusters.cns')
    parser.add_argument("--algorithm", default='OCG')
    parser.add_argument("--network", default='SPEPPI_PPI_interactome_monocytes_largest_connected_componant.txt')
    args = parser.parse_args()

    # Créer une instance de la classe Format_Data_cns
    data_formatter = Format_Data_cns(args.file_path, args.output, args.algorithm, args.network)
