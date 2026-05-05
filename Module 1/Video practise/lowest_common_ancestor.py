'''Module to find the lowest common ancestor of a BST'''

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
    class with solution function that finds the lowest common ancestor
    node of two given nodes in BST
    '''
    def lowestCommonAncestor(self, root: Treenode, p: Treenode, q: Treenode) -> Treenode:
        '''
        Finds lowest common ancestor node of two(different!!!) given nodes in BST
        '''
        while root:
            if p.val > root.val and q.val > root.val:
                root = root.right
            elif p.val < root.val and q.val < root.val:
                root = root.left
            else:
                return root
