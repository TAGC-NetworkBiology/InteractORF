import os
from optparse import OptionParser

from igraph import Graph

# ===========================================
# Information about file formats
# ===========================================

# Input and output files are expected to use the Large Graph Layout (LGL) format
# - .ncol extension should be used
# - The LGL is a space separated list of two connected nodes, 
#   with an optional third column of weight.
# - The file must not have any header line
# - Each line must be unique
# - A node may connect to many other nodes
# - A node cannot connect to itself
# - If a line is B-A, there cannot also be a line A-B
# - There cannot be blank lines
# - There cannot be blanks in any column


# ===========================================
# Methods
# ===========================================

## get_largest_connected_component
#  -------------------------------
#
# This method allows to extract the largest connected component 
# from a graph and write it into a file.
#
# @param merged_interactome: String - The path to the input file.
# @param largest_connected_component: String - The path to the output file.
# 
def get_largest_connected_component( merged_interactome, largest_connected_component ):
    
    # Import graph from file
    graph = Graph.Read_Ncol( f = merged_interactome,
                             names = True,
                             directed = False )
    
    # Calculates the weak clusters (connected components) for a given graph
    components = graph.clusters( mode = 'weak' )
    
    # Get and print the sizes of the components
    components_sizes = components.sizes()
    print( 'The graph contains ' + str( len( components_sizes ) ) + 
           ' weakly connected components which sizes are:\n' +
           ', '.join( map( str, components.sizes() ) ) + '.' )
    
    # Get the largest cluster of the clustered graph
    largest_component = components.giant()
    
    # Get the graph corresponding to the largest cluster
    largest_component_graph = graph.induced_subgraph( vertices = largest_component.vs["name"],
                                                      implementation = 'auto' )
    
    # Simplify this graph by removing self-loops and/or multiple edges
    largest_component_graph_simplified = largest_component_graph.simplify( multiple = True,
                                                                           loops = True,
                                                                           combine_edges = None )
    
    # Export the graph as ncol file
    largest_component_graph_simplified.write_ncol( f = largest_connected_component,
                                                   names = 'name',
                                                   weights = None )



# ===========================================
# Parse options and run script
# ===========================================

if __name__ == '__main__':
    
    merged_interactome = '05_Output/SPEPPI_PPI_interactome_monocytes.txt'
    largest_connected_component = '05_Output/SPEPPI_PPI_interactome_monocytes_largest_connected_componant.ncol'
    
    # Run the script
    print( 'INFO :: Starting the extraction of the largest connected component' )
    get_largest_connected_component( merged_interactome = merged_interactome,
                                     largest_connected_component = largest_connected_component )
    print( 'INFO :: The extraction of the largest connected component has finished' )