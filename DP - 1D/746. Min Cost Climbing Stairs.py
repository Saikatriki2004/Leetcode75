from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        # If there are only two steps, the answer is the minimum of the two
        if n == 2:
            return min(cost[0], cost[1])
        
        # dp array to store the minimum cost to reach each step
        dp = [0] * n
        
        # Base cases
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        # Fill the dp array
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        
        # The minimum cost to reach the top can be from the last step or the second last step
        return min(dp[n-1], dp[n-2])

# Example usage
if __name__ == "__main__":
    solution = Solution()
    print(solution.minCostClimbingStairs([10, 15, 20]))  # Output: 15
    print(solution.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))  # Output: 6
