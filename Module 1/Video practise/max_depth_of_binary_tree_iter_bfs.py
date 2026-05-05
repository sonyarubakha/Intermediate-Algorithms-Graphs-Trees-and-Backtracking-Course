'''Module to find max depth of binary tree using iterative BFS.'''

class Treenode:
    '''
    Definition for a binary tree node.
    '''
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    class with solution function on how to find the max depth of binary tree using iterative BFS.
    '''
    def maxDepth(self, root: Treenode) -> int:
        '''
        Calculetes max depth of binary tree using iterative BFS.
        '''
        if not root:
            return 0
        queue = [root]
        depth = 0
        while queue:
            depth +=1
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth
