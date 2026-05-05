'''Module to find max depth of binary tree.'''

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
    class with solution function on how to fimd the max depth of binary tree.
    '''
    def maxDepth(self, root: Treenode) -> int:
        '''
        Calculetes max depth of binary tree.
        '''
        if not root:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return 1 + max(left_depth, right_depth)
