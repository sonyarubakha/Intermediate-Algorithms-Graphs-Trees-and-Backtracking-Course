'''Module to find out the order from alien language'''

def alienOrder(words):
    '''
    function to understand the order of letters in alien language
    using recursive DFS and graph.
    '''
    adj = {c: set() for word in words for c in word}
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i+1]
        minLen = min(len(word1), len(word2))
        if len(word1) > len(word2) and word1[:minLen] == word2[:minLen]:
            return ''
        for j in range(minLen):
            if word1[j] != word2[j]:
                adj[word1[j]].add(word2[j])
                break
    visited = {}
    order = []
    def dfs(c):
        if c in visited:
            return visited[c]
        visited[c] = False
        for nei in adj[c]:
            if dfs(nei) == False:
                return False
        visited[c] = True
        order.append(c)
        return True
    for c in adj:
        if c not in visited:
            if not dfs(c):
                return ''
    return ''.join(order[::-1])
