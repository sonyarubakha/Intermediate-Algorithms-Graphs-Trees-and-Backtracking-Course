'''Module to check if you can finish all courses when given an array of prerequisites.'''

class Solution:
    '''
    class with a solution function to check if you can finish all courses.
    '''
    def canFinish(self, n: int, prerequisites : list[list[int]]) -> bool:
        '''
        Checks if you can finish all n courses based on prerequisites using recursive DFS.
        '''
        graph = [[] for _ in range(n)]
        cycle = [False] * n
        for pair in prerequisites:
            graph[pair[0]].append(pair[1])
        def dfs(course):
            if cycle[course]:
                return False
            if graph[course] is None:
                return True
            cycle[course] = True
            for prereq in graph[course]:
                if dfs(prereq) is False:
                    return False
            cycle[course] = False
            graph[course] = []
            return True
        for i in range(n):
            if dfs(i) is False:
                return False
        return True
