'''Module to invert binary tree.'''

class TreeNode:
    '''
    Definition for a binary tree node.
    '''
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    class with solution on how to inert binary tree.
    '''
    def invertTree(self, root: TreeNode) -> TreeNode:
        '''
        Inverts binary tree.
        '''
        if root is None:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
