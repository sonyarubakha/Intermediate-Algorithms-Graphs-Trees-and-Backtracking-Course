'''Module to check whether the list of undirected edges makes up a valid tree.'''

def validTree(n, edges):
    '''
    Checks whether edges make up avalid tree using recursive DFS.
    Tree is a special graph, which is connected and has NO cycle.
    '''
    if len(edges) != n - 1:
        return False
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    visited = set()
    def dfs(node, parent):
        if node in visited:
            return False
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            path_clear = dfs(neighbor, node)
            if path_clear is False:
                return False
        return True
    return dfs(0, -1) and len(visited) == n
