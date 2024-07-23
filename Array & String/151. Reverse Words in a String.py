class Solution:
    def reverseWords(self, s):
        # Split the string by spaces and filter out empty strings
        words = s.split()
        # Reverse the list of words
        reversed_words = words[::-1]
        # Join the reversed list into a single string with a single space separator
        return ' '.join(reversed_words)

# Example usage:
solution = Solution()
print(solution.reverseWords("the sky is blue"))      # Output: "blue is sky the"
print(solution.reverseWords("  hello world  "))       # Output: "world hello"
print(solution.reverseWords("a good   example"))      # Output: "example good a"
