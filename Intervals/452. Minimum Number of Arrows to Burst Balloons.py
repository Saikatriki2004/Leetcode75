from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        # Sort balloons by their end position
        points.sort(key=lambda x: x[1])
        
        # Initialize the number of arrows needed
        arrows = 0
        last_end = float('-inf')
        
        # Iterate through sorted balloons
        for start, end in points:
            if start > last_end:
                # If the current balloon starts after the last arrow position, shoot a new arrow
                arrows += 1
                last_end = end
        
        return arrows

# Example usage
solution = Solution()
points = [[10,16],[2,8],[1,6],[7,12]]
print(solution.findMinArrowShots(points))  # Output: 2

points = [[1,2],[3,4],[5,6],[7,8]]
print(solution.findMinArrowShots(points))  # Output: 4

points = [[1,2],[2,3],[3,4],[4,5]]
print(solution.findMinArrowShots(points))  # Output: 2
