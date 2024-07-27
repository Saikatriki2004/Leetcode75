from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # Sort intervals based on their end times
        intervals.sort(key=lambda x: x[1])
        
        # Initialize variables
        last_end = float('-inf')  # Last end time of the interval added to the result
        remove_count = 0  # Count of intervals to remove
        
        # Iterate through sorted intervals
        for interval in intervals:
            start, end = interval
            if start < last_end:
                # If there is an overlap, increment the count of intervals to remove
                remove_count += 1
            else:
                # Update last_end to the end time of the current interval
                last_end = end
        
        return remove_count

# Example usage
solution = Solution()
intervals = [[1,2],[2,3],[3,4],[1,3]]
print(solution.eraseOverlapIntervals(intervals))  # Output: 1

intervals = [[1,2],[1,2],[1,2]]
print(solution.eraseOverlapIntervals(intervals))  # Output: 2

intervals = [[1,2],[2,3]]
print(solution.eraseOverlapIntervals(intervals))  # Output: 0
