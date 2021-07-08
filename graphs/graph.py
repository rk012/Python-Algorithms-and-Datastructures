class Graph:
    def __init__(self, isDirected):
        self.isDirected = isDirected
        self.nodes = []
        self.adj_list = []
        self.adj_matrix = []

    def addNode(self):
        self.nodes.append(len(self.nodes))
        self.adj_list.append([])
        for i in range(0, len(self.adj_matrix)):
            self.adj_matrix[i].append(0)
        self.adj_matrix.append([0 for x in range(0, len(self.nodes))])

    def addEdge(self, node0, node1):
        self.adj_list[node0].append(node1)
        self.adj_matrix[node0][node1] = 1

        if not self.isDirected:
            self.adj_list[node1].append(node0)
            self.adj_matrix[node1][node0] = 1

    def getNodes(self):
        return self.nodes

    def getAdjacencyMatrix(self):
        return self.adj_matrix

    def getAdjacencyList(self):
        return self.adj_list


def invertAdjacencyList(adjacencylist):
    newlist = [[] for x in range(0, len(adjacencylist))]
    for i in range(0, len(adjacencylist)):
        for j in range(0, len(adjacencylist[i])):
            newlist[adjacencylist[i][j]].append(i)

    return newlist

def invertAdjacencyMatrix(adjacencymatrix):
    newmatrix = adjacencymatrix
    for i in range(0, len(adjacencymatrix)):
        for j in range(0, len(adjacencymatrix[i])):
            newmatrix[j][i] = adjacencymatrix[i][j]

    return newmatrix
