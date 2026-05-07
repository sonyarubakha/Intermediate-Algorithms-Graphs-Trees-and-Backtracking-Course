'''
Module to return number of islands from binary grid.
Islands are represented by `1`s
'''

class Solution:
    '''
    class with solution function to count islands of 1`s in a binary grid.
    '''
    def numIslands(self, grid: list[list[str]]) -> int:
        '''
        Counts number of islands(areas of 1`s surrounded by 0`s) using recursive DFS.
        '''
        if not grid:
            return 0
        def dfs(i, j):
            if (i < 0 or i >= len(grid) or
                j < 0 or j >= len(grid[0]) or
                grid[i][j] == '0'):
                return
            grid[i][j] = '0'
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count
