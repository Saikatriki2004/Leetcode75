class Solution:
    def decodeString(self, s: str) -> str:
        # Stacks to keep track of characters and multipliers
        char_stack = []
        num_stack = []
        current_num = 0
        current_string = ""

        for char in s:
            if char.isdigit():
                # Build the number for the multiplier
                current_num = current_num * 10 + int(char)
            elif char == '[':
                # Push the current number and string onto their respective stacks
                num_stack.append(current_num)
                char_stack.append(current_string)
                # Reset for the new substring
                current_num = 0
                current_string = ""
            elif char == ']':
                # Pop the number and previous string
                prev_string = char_stack.pop()
                repeat_count = num_stack.pop()
                # Build the new substring
                current_string = prev_string + (current_string * repeat_count)
            else:
                # Add the character to the current substring
                current_string += char

        return current_string
# Create an instance of the Solution class
solution = Solution()

# Example 1
s1 = "3[a]2[bc]"
print(solution.decodeString(s1))  # Output: "aaabcbc"

# Example 2
s2 = "3[a2[c]]"
print(solution.decodeString(s2))  # Output: "accaccacc"

# Example 3
s3 = "2[abc]3[cd]ef"
print(solution.decodeString(s3))  # Output: "abcabccdcdcdef"
