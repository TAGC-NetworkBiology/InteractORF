if (!require("BiocManager", quietly = TRUE))
  install.packages("BiocManager")

BiocManager::install("rrvgo")


# Charger les données depuis le fichier CSV
data <- HighQualityGraph_LargestComponent_partition_BP
clusters_info <- readLines("~/Bureau/Interactome_sORF_monocytes/07_OCG_interactome/05_Output/Enrichment_sORF_in_clusters.txt")

# Initialiser un dictionnaire pour stocker les valeurs de x pour chaque cluster
clusters <- list()

# Extraire les informations sur les clusters
for (line in clusters_info) {
  if (grepl("Cluster", line)) {
    cluster_id <- as.numeric(gsub("Cluster (\\d+):.*", "\\1", line))
    x_value <- as.numeric(gsub(".*x = (\\d+).*", "\\1", line))
    clusters[[cluster_id]] <- x_value
  }
}



# Supprimer les lignes correspondant aux clusters avec x = 0
for (cluster_id in seq_along(clusters)) {
  if (clusters[[cluster_id]] == 0) {
    data <- data[data$ClassID != cluster_id, ]
  }
}

data_parent <- HighQualityGraph_LargestComponent_partition_BP_cluster_with_one_or_more_sPEP_and_parent_term
# Créer une colonne "x_count" dans le fichier CSV avec le nombre de x pour chaque ClassID
data_parent$x_count <- sapply(data$ClassID, function(id) clusters[[id]])

# Sauvegarder le résultat dans un nouveau fichier CSV
write.csv(data_parent, "/home/slivak/Bureau/Interactome_sORF_monocytes/07_OCG_interactome/05_Output/HighQualityGraph.LargestComponent.partition.BP.cluster.with.one.or.more.sPEP.and.parent.term.csv", row.names = FALSE)

# Afficher le résultat final
print(data)

write.csv(data, file = "/home/slivak/Bureau/Interactome_sORF_monocytes/07_OCG_interactome/05_Output/HighQualityGraph.LargestComponent.partition.BP.cluster.with.one.or.more.sPEP.csv", row.names = FALSE)

# Filtrer les lignes avec HypergeometricLaw égale à True
data_filtre_majority_law <- subset(data, MajorityLaw == "True")



library(rrvgo)
simMatrix <- calculateSimMatrix(data_filtre_majority_law$GoTermID,
                                orgdb="org.Hs.eg.db",
                                ont="BP",
                                method="Rel")
write.csv(simMatrix, file = "/home/slivak/Bureau/Interactome_sORF_monocytes/07_OCG_interactome/05_Output/SimMatrix.csv", row.names = TRUE)

reducedTerms <- reduceSimMatrix(simMatrix,
                                threshold=0.5,
                                orgdb="org.Hs.eg.db")
write.csv(reducedTerms, file = "/home/slivak/Bureau/Interactome_sORF_monocytes/07_OCG_interactome/05_Output/Majority_Rule_parent_terms_inferred.csv", row.names = FALSE)
# Tracer le treemap
#reducedTerms <- head(reducedTerms, -1)
treemapPlot(reducedTerms)
