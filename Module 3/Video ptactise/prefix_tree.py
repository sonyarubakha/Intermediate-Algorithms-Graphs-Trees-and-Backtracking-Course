'''Module with realization of Trie(prefix tree.)'''

class Trienode:
    '''
    Definition for a prefix tree node.
    '''
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    '''
    Prefix tree class.
    '''
    def __init__(self):
        self.root = Trienode()


    def insert(self, word: str) -> None:
        '''
        Inserts the word in the prefix tree.
        '''
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] =Trienode()
            node = node.children[char]
        node.is_end = True


    def search(self, word: str) -> bool:
        '''
        Search the word in the Trie.
        True if word is in Trie, otherwise False.
        '''
        node = self.root
        for char in word:
            if char not in node.children:
                return None
            node = node.children[char]
        return node.is_end


    def startsWith(self, prefix: str) -> bool:
        '''
        Search string prefix in previously inserted word.
        '''
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node
