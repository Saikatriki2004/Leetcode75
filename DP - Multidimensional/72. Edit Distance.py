class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        
        # Create a (m+1) x (n+1) DP table
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Initialize the DP table
        for i in range(m + 1):
            dp[i][0] = i  # Minimum operations to convert word1[0:i] to empty word2
        for j in range(n + 1):
            dp[0][j] = j  # Minimum operations to convert empty word1 to word2[0:j]
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  # No additional cost if characters match
                else:
                    dp[i][j] = min(dp[i - 1][j] + 1,    # Delete
                                   dp[i][j - 1] + 1,    # Insert
                                   dp[i - 1][j - 1] + 1) # Replace
        
        # The result is the minimum number of operations to convert word1 to word2
        return dp[m][n]

# Example usage
solution = Solution()
print(solution.minDistance("horse", "ros"))       # Output: 3
print(solution.minDistance("intention", "execution")) # Output: 5
