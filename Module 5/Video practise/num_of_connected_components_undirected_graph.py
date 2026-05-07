'''Module to find out a number of connected components in an undirected graph.'''

def countComponents(n, edges):
    '''
    counts the number of connected components in an undirected graph
    when given an array of edges and number of vertices using recursive DFS.
    '''
    def dfs(node):
        if visited[node]:
            return
        visited[node] = True
        for neighbor in graph[node]:
            dfs(neighbor)
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    visited = [False] * n
    components = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            components += 1
    return components
