'''Module to check if one tree is a subtree for another tree.'''
from same_tree import Solution as SameTreeSolution
class Treenode:
    '''
    Definition for a binary tree node.
    '''
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(SameTreeSolution):
    '''
    class with solution function that checks if one tree is a subtree for another tree.
    '''
    def isSubtree(self, root: Treenode, subRoot: Treenode) -> bool:
        '''
        checks if one tree is a subtree for another tree.
        '''
        if subRoot is None:
            return True
        if not root and subRoot:
            return False
        if self.isSameTree(root, subRoot):
            return True
        left_check = self.isSubtree(root.left, subRoot)
        right_check = self.isSubtree(root.right, subRoot)
        return left_check or right_check
