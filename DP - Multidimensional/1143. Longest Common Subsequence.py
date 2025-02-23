class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Get the lengths of the input strings
        m, n = len(text1), len(text2)
        
        # Create a 2D dp array initialized with 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill the dp table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # The result is in the bottom-right cell of the dp array
        return dp[m][n]

# Example usage
solution = Solution()
print(solution.longestCommonSubsequence("abcde", "ace"))  # Output: 3
print(solution.longestCommonSubsequence("abc", "abc"))    # Output: 3
print(solution.longestCommonSubsequence("abc", "def"))    # Output: 0
