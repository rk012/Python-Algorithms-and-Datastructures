from graphs.graph import Graph, invertAdjacencyList


def bfs(start, end, adj_list):
    _adj_list = invertAdjacencyList(adj_list)

    scores = [-1 for x in _adj_list]
    scores[end] = 0

    path = [start]
    visited = [end]
    queue = [end]

    current_score = 0

    while len(queue) != 0:
        current_score += 1
        current_node = queue.pop(0)

        for x in _adj_list[current_node]:
            if x not in visited:
                scores[x] = current_score
                visited.append(x)
                queue.append(x)

        if start in visited:
            current_score -= 1
            while current_score > 0:
                for nextNode in adj_list[path[-1]]:
                    if scores[nextNode] == current_score - 1:
                        path.append(nextNode)
                        break
                current_score -= 1
            return path

    return False


if __name__ == "__main__":
    g = Graph(False)

    for x in range(0, 8):
        g.addNode()

    g.addEdge(0, 1)
    g.addEdge(1, 7)
    g.addEdge(7, 3)
    g.addEdge(3, 1)
    g.addEdge(0, 2)
    g.addEdge(2, 4)
    g.addEdge(4, 3)
    g.addEdge(4, 5)
    g.addEdge(6, 4)

    print(bfs(6, 7, g.getAdjacencyList()))
