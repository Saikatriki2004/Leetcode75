class Solution:
    def minEatingSpeed(self, piles, h):
        def canEatAllBananas(speed):
            hours = 0
            for pile in piles:
                hours += (pile + speed - 1) // speed  # Calculate hours needed for current pile
            return hours <= h
        
        # Initialize binary search bounds
        low, high = 1, max(piles)
        
        while low <= high:
            mid = (low + high) // 2
            if canEatAllBananas(mid):
                high = mid - 1
            else:
                low = mid + 1
        
        return low

# Example usage
solution = Solution()
print(solution.minEatingSpeed([3, 6, 7, 11], 8))  # Output: 4
print(solution.minEatingSpeed([30, 11, 23, 4, 20], 5))  # Output: 30
print(solution.minEatingSpeed([30, 11, 23, 4, 20], 6))  # Output: 23
