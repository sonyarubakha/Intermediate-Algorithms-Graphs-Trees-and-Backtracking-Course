'''Module to deserialize a binary tree.'''

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
    class with function to convert a string into a binary tree.
    '''
    def deserialize(self, data):
        '''
        decodes your encoded data to a tree.
        '''
        if not data:
            return None
        values = data.split(',')
        root = Treenode(int(values[0]))
        queue = [root]
        i = 1
        while queue:
            node = queue.pop(0)
            if values[i] != 'N':
                node.left = Treenode(int(values[i]))
                queue.append(node.left)
            i += 1
            if values[i] != 'N':
                node.right = Treenode(int(values[i]))
                queue.append(node.right)
            i += 1
        return root
