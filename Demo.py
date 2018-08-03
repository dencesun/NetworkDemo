# -*- coding:utf-8

import networkx as nx


def getDegree(graph, node):
    return graph.degree(node)


def getNumberOfNodes(graph):
    pass


def getNumberofEdges(graph):
    pass


if __name__ == '__main__':

    graph = nx.Graph()
    graph.add_edge(1,2)
    graph.add_edge(2,3)
    print(getDegree(graph, 1))

