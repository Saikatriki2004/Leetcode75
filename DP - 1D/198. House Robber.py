from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Edge case: If there are no houses
        if not nums:
            return 0
        
        # Edge case: If there is only one house
        if len(nums) == 1:
            return nums[0]
        
        # Create a dp array where dp[i] represents the maximum amount of money that can be robbed up to the i-th house
        dp = [0] * len(nums)
        
        # Base cases
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        # Fill the dp array
        for i in range(2, len(nums)):
            # For each house i, decide whether to rob it or not
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        # The answer will be the maximum amount that can be robbed up to the last house
        return dp[-1]

# Example usage
if __name__ == "__main__":
    solution = Solution()
    print(solution.rob([1, 2, 3, 1]))  # Output: 4
    print(solution.rob([2, 7, 9, 3, 1]))  # Output: 12
