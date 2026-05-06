'''Module to construct a binary tree from preorder & inorder traversal'''

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
    class with solution functions to construct a binary tree
    from preorder & inorder traversal
    '''
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Treenode:
        '''
        builds a binary tree from results of preorder AND inorder traversals.
        '''
        io_map = {}
        for i in range(len(inorder)):
            io_map[inorder[i]] = i
        return self.splitTree(preorder, io_map, 0, 0, len(inorder)-1)

    def splitTree(self, preorder, io_map, rootIndex, left, right):
        '''
        determines the tree structure by splitting traversals
        '''
        if left > right:
            return None
        root = Treenode(preorder[rootIndex])
        mid = io_map[preorder[rootIndex]]
        if mid > left:
            root.left = self.splitTree(preorder, io_map, rootIndex+1, left, mid-1)
        if mid < right:
            root.right = self.splitTree(preorder, io_map, rootIndex+mid-left+1, mid+1, right)
        return root
