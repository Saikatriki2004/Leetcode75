from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations, values, queries):
        # Step 1: Build the graph
        graph = defaultdict(dict)
        for (start, end), value in zip(equations, values):
            graph[start][end] = value
            graph[end][start] = 1 / value
        
        def bfs(start, end):
            if start not in graph or end not in graph:
                return -1.0
            # BFS to find the path from start to end
            queue = deque([(start, 1.0)])
            visited = set()
            while queue:
                node, value = queue.popleft()
                if node == end:
                    return value
                visited.add(node)
                for neighbor, weight in graph[node].items():
                    if neighbor not in visited:
                        queue.append((neighbor, value * weight))
            return -1.0
        
        # Step 2: Process each query
        result = []
        for start, end in queries:
            result.append(bfs(start, end))
        
        return result

# Example usage:
solution = Solution()
print(solution.calcEquation(
    [["a","b"],["b","c"]],
    [2.0, 3.0],
    [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
))  # Output: [6.0, 0.5, -1.0, 1.0, -1.0]

print(solution.calcEquation(
    [["a","b"],["b","c"],["bc","cd"]],
    [1.5, 2.5, 5.0],
    [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
))  # Output: [3.75, 0.4, 5.0, 0.2]

print(solution.calcEquation(
    [["a","b"]],
    [0.5],
    [["a","b"],["b","a"],["a","c"],["x","y"]]
))  # Output: [0.5, 2.0, -1.0, -1.0]
