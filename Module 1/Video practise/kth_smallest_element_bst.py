'''Module to find the kth smallest element in a BST'''

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
    class with solution function that finds the kth smallest
    element(1-indexed) in a BST.
    '''
    def kthSmallest(self, root: Treenode, k: int) -> int:
        '''
        Given the root of a BST and an int k, returns the kth
        smallest value(1-indexed) of all values of the nodes in the tree
        '''
        io_list = []
        self.helper(root, io_list)
        return io_list[k-1]

    def helper(self, tree_node, io_list):
        '''
        helper function that traverses the BST in
        in-order traversal.
        '''
        if tree_node is None:
            return
        self.helper(tree_node.left, io_list)
        io_list.append(tree_node.val)
        self.helper(tree_node.right, io_list)
