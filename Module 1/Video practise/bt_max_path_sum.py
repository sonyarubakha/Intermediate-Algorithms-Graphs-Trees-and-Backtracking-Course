'''Module to find the max path sum of any non-empty path.'''

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
    class with solution function that finds the max non-empty path
    and returns the sum of that path.
    '''
    def maxPathSum(self, root: Treenode | None) -> int:
        '''
        finds the max non-empty path and returns the sum of that path
        using recursive DFS.
        '''
        max_sum = float('-inf')
        def dfs(node):
            if not node:
                return 0
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)
            price_newpath = node.val + left_gain + right_gain
            max_sum = max(max_sum, price_newpath)
            return node.val + max(left_gain, right_gain)
        dfs(root)
        return max_sum
