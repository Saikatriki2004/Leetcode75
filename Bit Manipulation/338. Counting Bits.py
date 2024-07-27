from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        # Initialize the list with zeros
        ans = [0] * (n + 1)
        
        # Compute the number of 1's for each number from 1 to n
        for i in range(1, n + 1):
            ans[i] = ans[i // 2] + (i % 2)
        
        return ans

# Example usage
solution = Solution()
print(solution.countBits(2))  # Output: [0, 1, 1]
print(solution.countBits(5))  # Output: [0, 1, 1, 2, 1, 2]
