'''Module to check if two trees are the same.'''

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
    class with solution function that checks if two trees are the same.
    '''
    def isSameTree(self, p: Treenode | None, q: Treenode | None) -> bool:
        '''
        checks if two trees are the same
        '''
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        left_compare = self.isSameTree(p.left, q.left)
        right_compare = self.isSameTree(p.right, q.right)
        return left_compare and right_compare
