class Solution:
    def minReorder(self, n, connections):
        from collections import defaultdict, deque

        # Create adjacency lists for both directions
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append((v, True))  # (destination, isReversed)
            graph[v].append((u, False)) # (destination, isReversed)

        def dfs(node):
            # Start DFS
            stack = [node]
            visited = set()
            reversals = 0
            
            while stack:
                curr = stack.pop()
                if curr in visited:
                    continue
                visited.add(curr)
                
                for neighbor, isReversed in graph[curr]:
                    if neighbor not in visited:
                        if isReversed:
                            reversals += 1
                        stack.append(neighbor)
                        
            return reversals
        
        return dfs(0)

# Example usage:
solution = Solution()
print(solution.minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]))  # Output: 3
print(solution.minReorder(5, [[1,0],[1,2],[3,2],[3,4]]))       # Output: 2
print(solution.minReorder(3, [[1,0],[2,0]]))                    # Output: 0
