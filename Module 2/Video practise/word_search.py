'''Module to check if woard exists in the grid.'''

class Solution:
    '''
    class with solution function that checks if word exists in the grid.
    '''
    def exist(self, board: list[list[str]], word: str) -> bool:
        '''
        checks if word exists in the grid by using recursive DFS.
        '''
        def dfs(i, j, k):
            if k == len(word):
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
                return False
            tmp, board[i][j] = board[i][j], '/'
            result = dfs(i+1, j, k+1) or dfs(i-1, j, k+1) or dfs(i, j+1, k+1) or dfs(i, j-1, k+1)
            board[i][j] = tmp
            return result
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False
