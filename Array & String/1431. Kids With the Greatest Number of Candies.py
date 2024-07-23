class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        # Step 1: Find the current maximum number of candies
        max_candies = max(candies)
        
        # Step 2: Check if adding extraCandies to each kid's candies will make it the greatest or not
        result = [(candy + extraCandies) >= max_candies for candy in candies]
        
        return result

# Example usage:
solution = Solution()
print(solution.kidsWithCandies([2,3,5,1,3], 3))  # Output: [True, True, True, False, True]
print(solution.kidsWithCandies([4,2,1,1,2], 1))  # Output: [True, False, False, False, False]
print(solution.kidsWithCandies([12,1,12], 10))   # Output: [True, False, True]
