class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')  # Set of vowel characters
        max_vowels = 0
        current_vowels = 0
        
        # Count vowels in the initial window of length k
        for i in range(k):
            if s[i] in vowels:
                current_vowels += 1
        
        max_vowels = current_vowels
        
        # Slide the window across the string
        for i in range(k, len(s)):
            if s[i] in vowels:
                current_vowels += 1
            if s[i - k] in vowels:# Create an instance of the Solution class
solution = Solution()

# Example 1
s1 = "abciiidef"
k1 = 3
print(solution.maxVowels(s1, k1))  # Output: 3

# Example 2
s2 = "aeiou"
k2 = 2
print(solution.maxVowels(s2, k2))  # Output: 2

# Example 3
s3 = "leetcode"
k3 = 3
print(solution.maxVowels(s3, k3))  # Output: 2

                current_vowels -= 1
            max_vowels = max(max_vowels, current_vowels)
        
        return max_vowels
