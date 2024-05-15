import pandas as pd

# Charger les données depuis le fichier CSV
df = pd.read_csv('01_Reference/HighQualityGraph.LargestComponent.partition.BP.csv')

# Nombre de termes uniques dans la colonne 'GoTermID'
nb_termes_uniques = df['GoTermID'].nunique()

# Filtrer les lignes avec l'annotation 'True' dans la colonne 'MajorityLaw'
annotations_majority_true = df[df['MajorityLaw'] == True]

# Nombre de termes uniques dans la colonne 'GoTermID' avec l'annotation 'True' dans 'MajorityLaw'
nb_termes_uniques_majority_true = annotations_majority_true['GoTermID'].nunique()

# Filtrer les lignes avec l'annotation 'True' dans la colonne 'HypergeometricLaw'
annotations_hypergeometric_true = df[df['HypergeometricLaw'] == True]

# Nombre de termes uniques dans la colonne 'GoTermID' avec l'annotation 'True' dans 'HypergeometricLaw'
nb_termes_uniques_hypergeometric_true = annotations_hypergeometric_true['GoTermID'].nunique()

print("Nombre de termes uniques dans la colonne 'GoTermID':", nb_termes_uniques)
print("Nombre de termes uniques dans la colonne 'GoTermID' avec l'annotation 'True' dans 'MajorityLaw':", nb_termes_uniques_majority_true)
print("Nombre de termes uniques dans la colonne 'GoTermID' avec l'annotation 'True' dans 'HypergeometricLaw':", nb_termes_uniques_hypergeometric_true)


#####################Calcul pour les clusters possédant au moins 1 sPEP################################################

# Charger les données depuis le fichier CSV
df_with_sORF = pd.read_csv('05_Output/HighQualityGraph.LargestComponent.partition.BP.cluster.with.one.or.more.sPEP.csv', sep=',')

# Nombre de termes uniques dans la colonne 'GoTermID'
nb_termes_uniques = df_with_sORF['GoTermID'].nunique()

# Filtrer les lignes avec l'annotation 'True' dans la colonne 'MajorityLaw'
annotations_majority_true = df_with_sORF[df_with_sORF['MajorityLaw'] == 'True']

# Nombre de termes uniques dans la colonne 'GoTermID' avec l'annotation 'True' dans 'MajorityLaw'
nb_termes_uniques_majority_true = annotations_majority_true['GoTermID'].nunique()

# Filtrer les lignes avec l'annotation 'True' dans la colonne 'HypergeometricLaw'
annotations_hypergeometric_true = df_with_sORF[df_with_sORF['HypergeometricLaw'] == True]

# Nombre de termes uniques dans la colonne 'GoTermID' avec l'annotation 'True' dans 'HypergeometricLaw'
nb_termes_uniques_hypergeometric_true = annotations_hypergeometric_true['GoTermID'].nunique()

print("Nombre de termes uniques dans la colonne 'GoTermID' pour les clusters possédant au moins 1 SPEP:", nb_termes_uniques)
print("Nombre de termes uniques dans la colonne 'GoTermID' avec l'annotation 'True' dans 'MajorityLaw' pour les clusters possédant au moins 1 SPEP:", nb_termes_uniques_majority_true)
print("Nombre de termes uniques dans la colonne 'GoTermID' avec l'annotation 'True' dans 'HypergeometricLaw' pour les clusters possédant au moins 1 SPEP:", nb_termes_uniques_hypergeometric_true)

##################### Calcul pour les clusters significativements enrichis################################
# Définir les valeurs de 'ClassID' à filtrer
valeurs_a_filtrer = [14, 21, 63, 112, 113, 114, 278, 302]

# Filtrer les lignes où 'ClassID' est l'une des valeurs spécifiées
df_subset = df[df['ClassID'].isin(valeurs_a_filtrer)]

# Nombre de termes uniques dans la colonne 'GoTermID'
nb_termes_uniques = df_subset['GoTermID'].nunique()

# Filtrer les lignes avec l'annotation 'True' dans la colonne 'MajorityLaw'
annotations_majority_true = df_subset[df_subset['MajorityLaw'] == True]

# Nombre de termes uniques dans la colonne 'GoTermID' avec l'annotation 'True' dans 'MajorityLaw'
nb_termes_uniques_majority_true = annotations_majority_true['GoTermID'].nunique()

# Filtrer les lignes avec l'annotation 'True' dans la colonne 'HypergeometricLaw'
annotations_hypergeometric_true = df_subset[df_subset['HypergeometricLaw'] == True]

# Nombre de termes uniques dans la colonne 'GoTermID' avec l'annotation 'True' dans 'HypergeometricLaw'
nb_termes_uniques_hypergeometric_true = annotations_hypergeometric_true['GoTermID'].nunique()

print("Nombre de termes uniques dans la colonne 'GoTermID' pour les clusters significativement enrichis:", nb_termes_uniques)
print("Nombre de termes uniques dans la colonne 'GoTermID' avec l'annotation 'True' dans 'MajorityLaw' pour les clusters significativement enrichis:", nb_termes_uniques_majority_true)
print("Nombre de termes uniques dans la colonne 'GoTermID' avec l'annotation 'True' dans 'HypergeometricLaw' pour les clusters significativement enrichis:", nb_termes_uniques_hypergeometric_true)

####################################Associer un parent term au GO inferré#########################################
# Lire le premier fichier CSV et créer le dictionnaire GO -> ParentTerm
parent_term = pd.read_csv("05_Output/Majority_Rule_parent_terms_inferred.csv", delimiter=',')
go_parent_dict = dict(zip(parent_term['go'], parent_term['parentTerm']))

# Lire le deuxième fichier CSV

# Ajouter une nouvelle colonne "Parent term" en utilisant le dictionnaire
df_with_sORF['Parent term'] = df_with_sORF['GoTermID'].map(go_parent_dict)

# Sauvegarder le résultat dans un nouveau fichier CSV
#df_with_sORF.to_csv("05_Output/HighQualityGraph.LargestComponent.partition.BP.cluster.with.one.or.more.sPEP.and.parent.term.csv", index=False)

#######################################Combien de sPEP sont présent dans 1 terme GO##########################


df_with_sORF = pd.read_csv("05_Output/HighQualityGraph.LargestComponent.partition.BP.cluster.with.one.or.more.sPEP.and.parent.term.csv")

final_data = []

# Grouper les données par ClassID et Parent term, puis calculer la somme de nb_sPEPs pour chaque groupe
grouped = df_with_sORF.groupby(['ClassID', 'Parent term'])['nb_sPEPs'].sum().reset_index()

# Créer un dictionnaire pour stocker les valeurs uniques de nb_sPEPs pour chaque Parent term
parent_terms = {}
for index, row in grouped.iterrows():
    if row['Parent term'] not in parent_terms:
        parent_terms[row['Parent term']] = row['nb_sPEPs']
    else:
        parent_terms[row['Parent term']] += row['nb_sPEPs']

# Remplir la liste final_data avec les dictionnaires des valeurs uniques de Parent term et les sommes correspondantes de nb_sPEPs
for parent_term, nb_sPEPs in parent_terms.items():
    final_data.append({'Parent term': parent_term, 'occurence_annotation': nb_sPEPs})

# Créer le DataFrame final à partir de la liste final_data
final_df = pd.DataFrame(final_data)

final_df.to_csv("05_Output/comptage_nb_sPEP_fonctions_inferrees.csv", index=False)
