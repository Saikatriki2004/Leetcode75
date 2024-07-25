# Mocking the guess API for demonstration purposes.
# In a real scenario, this function will be provided.
def guess(num: int) -> int:
    if num == pick:
        return 0
    elif num < pick:
        return 1
    else:
        return -1

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            result = guess(mid)
            if result == 0:
                return mid
            elif result == -1:
                right = mid - 1
            else:
                left = mid + 1
        return -1  # This line should never be reached if the input is valid

# Example usage:
# Set the pick for testing purposes
pick = 6  # You can change this value for different test cases
solution = Solution()
print(solution.guessNumber(10))  # Expected output: 6
