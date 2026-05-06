'''Module to serialize a binary tree.'''

class Treenode:
    '''
    Definition for a binary tree node.
    '''
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    '''
    class with function to convert a binary tree into  string.
    '''
    def serialize(self, root):
        '''
        encodes a tree to a single string.
        '''
        if not root:
            return ''
        queue = [root]
        result = []
        while queue:
            node = queue.pop(0)
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append('N')
        return ','.join(result)
