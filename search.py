'''
The O(nlog(n)) time algorithm for calculating the search number of a tree
given in [1].

[1]: The Complexity of Searching a Graph. N. Megiddo et. al.
'''
import networkx as nx

def info(tree, root):
    '''
    Given an input of a tree graph, calculates the root's info 
    as in [1]. This function is recursive.

    INPUT
    tree: A networkx tree graph
    root: A vertex from tree that is the current root of tree

    OUTPUT
    treeInfo: The info for the current tree.
    '''
    
    #Calculate the degree of the root
    degree = nx.degree(tree, root)
    
    #Use reroot if the deg is 1 and merges otherwise
    if degree == 1:

        #A single edge has search number = 1
        if isEdge(tree):
            return ['E', 1, None]

        #Since tree is not an edge, we re-root and keep going
        return re-root(tree, root)
    else:

def computeInfo(tree):
    '''
    Given an input of a tree computes
    [type, s(T), M-info(T)]

    INPUT
    tree: A networkx tree graph

    OUTPUT
    info [type, s(T), M-info(T)]: See page 8 of [1].
    '''

    #Make the root the first node
    root = tree.nodes()[0]
    
    #Get the info for tree
    information = info(tree, root)

    return information
