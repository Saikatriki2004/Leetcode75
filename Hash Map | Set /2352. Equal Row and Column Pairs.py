from collections import defaultdict

class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        n = len(grid)
        
        # Create dictionaries to count occurrences of row and column tuples
        row_count = defaultdict(int)
        col_count = defaultdict(int)
        
        # Count occurrences of each row
        for row in grid:
            row_tuple = tuple(row)
            row_count[row_tuple] += 1
        
        # Count occurrences of each column
        for c in range(n):
            col_tuple = tuple(grid[r][c] for r in range(n))
            col_count[col_tuple] += 1
        
        # Calculate number of equal row and column pairs
        result = 0
        for row_tuple, row_occurrences in row_count.items():
            if row_tuple in col_count:
                result += row_occurrences * col_count[row_tuple]
        
        return result
# Create an instance of the Solution class
solution = Solution()

# Example 1
grid1 = [[3,2,1],[1,7,6],[2,7,7]]
print(solution.equalPairs(grid1))  # Output: 1

# Example 2
grid2 = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
print(solution.equalPairs(grid2))  # Output: 3
