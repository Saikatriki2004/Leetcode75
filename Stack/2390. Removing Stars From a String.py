class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char == '*':
                if stack:
                    stack.pop()  # Remove the closest non-star character
            else:
                stack.append(char)  # Add character to stack
        
        # Join the stack to form the resultant string
        return ''.join(stack)
# Create an instance of the Solution class
solution = Solution()

# Example 1
s1 = "leet**cod*e"
print(solution.removeStars(s1))  # Output: "lecoe"

# Example 2
s2 = "erase*****"
print(solution.removeStars(s2))  # Output: ""
