from collections import deque

class Solution:
    def nearestExit(self, maze, entrance):
        rows, cols = len(maze), len(maze[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        queue = deque([(entrance[0], entrance[1], 0)])  # (row, col, steps)
        visited = set()
        visited.add((entrance[0], entrance[1]))
        
        while queue:
            r, c, steps = queue.popleft()
            
            # Check if current cell is an exit (and not the entrance)
            if (r != entrance[0] or c != entrance[1]) and (r == 0 or r == rows - 1 or c == 0 or c == cols - 1):
                return steps
            
            # Explore the 4 possible directions
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == '.' and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc, steps + 1))
        
        return -1
if __name__ == "__main__":
    sol = Solution()
    maze = [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]]
    entrance = [1, 2]
    print(sol.nearestExit(maze, entrance))  # Output: 1

    maze = [["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]]
    entrance = [1, 0]
    print(sol.nearestExit(maze, entrance))  # Output: 2

    maze = [[".", "+"]]
    entrance = [0, 0]
    print(sol.nearestExit(maze, entrance))  # Output: -1
