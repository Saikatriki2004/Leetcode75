class Solution:
    def findCircleNum(self, isConnected):
        def dfs(city):
            # Mark the city as visited
            visited[city] = True
            # Visit all the connected cities
            for neighbor in range(len(isConnected)):
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor)
        
        n = len(isConnected)
        visited = [False] * n
        provinces = 0
        
        # Check each city
        for i in range(n):
            if not visited[i]:
                # Start a new DFS if this city hasn't been visited
                dfs(i)
                provinces += 1
        
        return provinces

# Example usage:
solution = Solution()
print(solution.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))  # Output: 2
print(solution.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]))  # Output: 3
