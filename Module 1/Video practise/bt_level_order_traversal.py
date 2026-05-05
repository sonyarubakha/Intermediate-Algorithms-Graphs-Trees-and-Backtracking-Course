'''Module to traverse on binary tree in level order.'''

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
    class with solution function that traverses on binary tree
    using in level order.
    '''
    def levelOrder(self, root: Treenode) -> list[list[int]]:
        '''
        traverses on binary tree using in level order.
        '''
        if not root:
            return []
        result, queue = [], [root]
        while queue:
            level_size = len(queue)
            level = []
            for _ in range(level_size):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result
