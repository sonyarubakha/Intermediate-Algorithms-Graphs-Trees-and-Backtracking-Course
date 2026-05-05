'''Module to find max depth of binary tree using iterative DFS.'''

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
    class with solution function on how to find the max depth of binary tree using iterative DFS.
    '''
    def maxDepth(self, root: Treenode) -> int:
        '''
        Calculetes max depth of binary tree using iterative DFS.
        '''
        if not root:
            return 0
        stack = [(root, 1)]
        max_depth = 0
        while stack:
            node, depth = stack.pop()
            if node:
                max_depth = max(max_depth, depth)
                if node.left:
                    stack.append((node.left, depth + 1))
                if node.right:
                    stack.append((node.right, depth + 1))
        return max_depth
