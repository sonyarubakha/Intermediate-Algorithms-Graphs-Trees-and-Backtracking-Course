'''Module to to find a combination of elements of array that in sum are equal to target integer.'''

class Solution:
    '''
    class with a solution function that finds all non-repetive combinations
    of elements in array to be equal in sum to target integer.
    '''
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        '''
        unction that finds all non-repetive combinations
        of elements in array to be equal in sum to target integer using recursive DFS.
        '''
        all_combinations = []
        def dfs(index, current_combination, current_sum):
            if current_sum == target:
                all_combinations.append(current_combination)
                return
            if index >= len(candidates) or current_sum > target:
                return
            dfs(index, current_combination + [candidates[index]], current_sum + candidates[index])
            dfs(index + 1, current_combination, current_sum)
        dfs(0, [], 0)
        return all_combinations
