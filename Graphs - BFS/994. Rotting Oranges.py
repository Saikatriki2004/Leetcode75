from collections import deque

class Solution:
    def orangesRotting(self, grid):
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        
        # Initialize the BFS queue and count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
        
        # If there are no fresh oranges, return 0
        if fresh_count == 0:
            return 0
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        minutes = 0
        
        # Perform BFS
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        fresh_count -= 1
            
            minutes += 1
        
        # If there are still fresh oranges, return -1
        return minutes - 1 if fresh_count == 0 else -1

# Example usage:
sol = Solution()
grid1 = [[2,1,1],[1,1,0],[0,1,1]]
print(sol.orangesRotting(grid1))  # Output: 4

grid2 = [[2,1,1],[0,1,1],[1,0,1]]
print(sol.orangesRotting(grid2))  # Output: -1

grid3 = [[0,2]]
print(sol.orangesRotting(grid3))  # Output: 0
