from graphs.graph import Graph


def dfs(start, end, adj_list):
    visited = [start]
    stack = [start]

    while len(stack) != 0:
        current_node = stack.pop()
        for x in adj_list[current_node]:
            if x not in visited:
                visited.append(x)
                stack.append(x)
        if end in visited:
            return True

    return False


if __name__ == "__main__":
    g = Graph(True)

    for i in range(0, 6):
        g.addNode()

    g.addEdge(0, 3)
    g.addEdge(1, 0)
    g.addEdge(1, 2)
    g.addEdge(3, 4)
    g.addEdge(3, 5)
    g.addEdge(4, 0)
    g.addEdge(5, 2)

    print(dfs(0, 1, g.getAdjacencyList()))
