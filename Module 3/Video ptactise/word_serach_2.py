'''Module to return all words from the board grid.'''

class Trienode:
    '''
    Definition for a prefix tree node.
    '''
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    '''
    class with functions that build grid with words using Trie
    and returning all words from the board grid.
    '''
    def buildTrie(self, words):
        '''
        Builds Trie(our grid board) with words.
        '''
        root = Trienode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = Trienode()
                node = node.children[char]
            node.is_end = True
        return root

    def dfs(self, board, node, i, j, path, result):
        '''
        DFS recursive.
        '''
        if node.is_end:
            result.add(path)
            node.is_end = False
        if (i < 0 or i >= len(board) or
            j < 0 or j >= len(board[0]) or
            board[i][j] not in node.children):
            return
        temp, board[i][j] = board[i][j], '#'
        for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            self.dfs(board, node.children[temp], x, y, path+temp, result)
        board[i][j] = temp


    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        '''
        finds and returns all words from the board.
        '''
        root = self.buildTrie(words)
        result = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in root.children:
                    self.dfs(board, root, i, j, '', result)
        return list(result)
