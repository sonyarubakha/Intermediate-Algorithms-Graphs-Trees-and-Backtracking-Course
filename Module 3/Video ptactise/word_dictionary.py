'''
Module with a data structure that supports adding new words and
finding if a string matches any previously added string.
'''

class Trienode:
    '''
    Definition for a prefix tree node.
    '''
    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:
    '''
    Word dictionary based on a prefix tree.
    '''
    def __init__(self):
        self.root = Trienode()

    def addWord(self, word: str) -> None:
        '''
        Adds word to the dictionary.
        '''
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] =Trienode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        '''
        Returns true if there is any string matches word.
        Word may contain dots `.` where dots can be matched with any letter.
        '''
        def dfs(node, i):
            if i == len(word):
                return node.is_end
            if word[i] == '.':
                for child in node.children.values():
                    if dfs(child, i+1):
                        return True
                return False
            if word[i] in node.children:
                return dfs(node.children[word[i]], i+1)
        return dfs(self.root, 0)
