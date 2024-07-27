from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0
        
        # Initialize states
        hold = -prices[0]  # Maximum profit if we hold a stock
        cash = 0  # Maximum profit if we do not hold a stock

        # Iterate through the days
        for price in prices[1:]:
            # Update the states
            new_hold = max(hold, cash - price)
            new_cash = max(cash, hold + price - fee)
            
            hold, cash = new_hold, new_cash
        
        # The result is the maximum profit when not holding any stock
        return cash

# Example usage
solution = Solution()
print(solution.maxProfit([1, 3, 2, 8, 4, 9], 2))  # Output: 8
print(solution.maxProfit([1, 3, 7, 5, 10, 3], 3)) # Output: 6
