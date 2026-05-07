'''Module to return a deep copy of a connected undirected graph.'''

class Node:
    '''
    Definition for a Node.
    '''
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors

class Solution:
    '''
    class with a solution function that makes a deep copy of a graph.
    '''
    def cloneGraph(self, node: 'Node') -> 'Node':
        '''
        Returns a deep copy of a connected undirected graph.
        '''
        if not node:
            return None
        cloned_nodes = {}
        queue = [node]
        cloned_nodes[node] = Node(node.val)
        while queue:
            current_node = queue.pop(0)
            for neighbor in current_node.neighbors:
                if neighbor not in cloned_nodes:
                    cloned_nodes[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                cloned_nodes[current_node].neighbors.append(cloned_nodes[neighbor])
        return cloned_nodes[node]
