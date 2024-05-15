import csv

def remove_duplicates(input_file, output_file):
    unique_proteins = set()
    with open(input_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row:  # Vérifier si la ligne n'est pas vide
                if row[0]:  # Vérifier si la première colonne n'est pas vide
                    unique_proteins.add(row[0])

    # Écrire les identifiants de protéine uniques dans un nouveau fichier CSV
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for protein in unique_proteins:
            writer.writerow([protein])


def fusionner_fichiers_csv(nom_fichier1, nom_fichier2, nom_fichier_sortie):
    # Liste pour stocker tous les identifiants
    identifiants = set()

    # Lire le premier fichier CSV et ajouter les identifiants à la liste
    with open(nom_fichier1, 'r') as fichier1:
        lecteur_csv = csv.reader(fichier1)
        for ligne in lecteur_csv:
            identifiants.add(ligne[0])

    # Lire le deuxième fichier CSV et ajouter les identifiants à la liste
    with open(nom_fichier2, 'r') as fichier2:
        lecteur_csv = csv.reader(fichier2)
        for ligne in lecteur_csv:
            identifiants.add(ligne[0])

    # Écrire tous les identifiants dans le fichier de sortie
    with open(nom_fichier_sortie, 'w', newline='') as fichier_sortie:
        ecrivain_csv = csv.writer(fichier_sortie)
        for identifiant in identifiants:
            ecrivain_csv.writerow([identifiant])

# Chemin du fichier d'entrée
input_file_all_monocytes = '01_Reference/Interactome_monocyte.csv'
input_file_intarcting_with_sORF_domain = '01_Reference/liste_proteines_interagissant_avec_domaines_sORFs.csv'
input_file_interacting_with_sORF_slim = '01_Reference/liste_proteines_interagissant_avec_slim_sORFs.csv'

# Chemin du fichier de sortie
output_file_all_monocytes = '01_Reference/liste_proteines_interactome_complet_monocytes_sans_doublons.csv'
output_file_interacting_with_sORF_domain ='01_Reference/liste_proteines_interagissant_avec_domaines_sORFs_sans_doublons.csv'
output_file_interacting_with_sORF_slim = '01_Reference/liste_proteines_interagissant_avec_slim_sORFs_sans_doublons.csv'
output_file_all_interacteurs_sORFs = '01_Reference/interacteurs_sORFs.csv'
output_file_all_interacteurs_sORFs_uniques = '01_Reference/interacteurs_sORFs_sans_doublons.csv'
# Appel de la fonction pour supprimer les doublons et créer le nouveau fichier
remove_duplicates(input_file_all_monocytes,output_file_all_monocytes)
remove_duplicates(input_file_intarcting_with_sORF_domain, output_file_interacting_with_sORF_domain)
remove_duplicates(input_file_interacting_with_sORF_slim, output_file_interacting_with_sORF_slim)
fusionner_fichiers_csv(output_file_interacting_with_sORF_domain, output_file_interacting_with_sORF_slim, output_file_all_interacteurs_sORFs)
remove_duplicates(output_file_all_interacteurs_sORFs, output_file_all_interacteurs_sORFs_uniques)
print("Les identifiants de protéines uniques ont été enregistrés")


#Rassembler la liste des interacteurs slim + domaines
