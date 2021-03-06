from heapq import heappop, heappush


def dijkstra(graph, start):
    """
    Uses Dijkstra's algortihm to find the shortest path between nodes in a graph.

    Parameters
    ----------
    graph : list[list[tuple]]
        A list of lists of adjacent vertices and their weights.
    start : int
        The vertex relative to which distances and paths are calculated.

    Returns
    -------
    dist : list[int]
        The relative distances of vertices relative to start.
    parents : list[int]
        The parent of a vertex on its path to start.
    """
    queue = [(0, start)]

    parents = [-1] * len(graph)
    visited = [False] * len(graph)
    dist = [float('inf')] * len(graph)

    dist[start] = 0

    while queue:
        path_len, v = heappop(queue)
        if not visited[v]:
            for (w, edge_len) in graph[v]:
                if (not visited[w]) and (edge_len + path_len < dist[w]):
                    dist[w], parents[w] = edge_len + path_len, v
                    heappush(queue, (edge_len + path_len, w))
            visited[v] = True

    return dist, parents


def find_path(start, end, parents):
    """
    Constructs a path between two vertices, given the parents of all vertices.

    Parameters
    ----------
    start : int
        The first verex in the path
    end : int
        The last vertex in the path
    parents : list[int]
        The parent of a vertex in its path from start to end.

    Returns
    -------
    path : list[int]
        The path from start to end.
    """
    path = []
    parent = end
    while parent != parents[start]:
        path.append(parent)
        parent = parents[parent]
    return path[::-1]
