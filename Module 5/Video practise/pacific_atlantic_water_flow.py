'''Module to return coordinates where rainwater can flow from one cell to both oceans'''

class Solution:
    '''
    class with a solution function to identify grid coordinates that can drain water
    to both the Pacific and Atlantic oceans.
    '''
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        '''
        Finds all grid coordinates from which rainwater can flow to both oceans using recursive DFS.
        '''
        if not heights:
            return []
        m, n = len(heights), len(heights[0])
        pacificReachable = [[False for _ in range(n)] for _ in range(m)]
        atlanticReachable = [[False for _ in range(n)] for _ in range(m)]
        def dfs(row, col, reachable):
            reachable[row][col] = True
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                newRow, newCol = row + dr, col + dc
                if (0 <= newRow < m and 0 <= newCol < n and not reachable[newRow][newCol] and
                heights[newRow][newCol] >= heights[row][col]):
                    dfs(newRow, newCol, reachable)
        for i in range(m):
            dfs(i, 0, pacificReachable)
            dfs(i, n - 1, atlanticReachable)
        for j in range(n):
            dfs(0, j, pacificReachable)
            dfs(m - 1, j, atlanticReachable)
        result = []
        for i in range(m):
            for j in range(n):
                if pacificReachable[i][j] and atlanticReachable[i][j]:
                    result.append([i, j])
        return result
