from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Step 1: Check if lengths are equal
        if len(word1) != len(word2):
            return False
        
        # Step 2: Count character frequencies
        count1 = Counter(word1)
        count2 = Counter(word2)
        
        # Step 3: Check if the set of characters in both words are the same
        if set(count1.keys()) != set(count2.keys()):
            return False
        
        # Step 4: Check if the sorted frequency counts are the same
        return sorted(count1.values()) == sorted(count2.values())
# Create an instance of the Solution class
solution = Solution()

# Example 1
word1 = "abc"
word2 = "bca"
print(solution.closeStrings(word1, word2))  # Output: True

# Example 2
word1 = "a"
word2 = "aa"
print(solution.closeStrings(word1, word2))  # Output: False

# Example 3
word1 = "cabbba"
word2 = "abbccc"
print(solution.closeStrings(word1, word2))  # Output: True
