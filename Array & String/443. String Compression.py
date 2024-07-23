class Solution:
    def compress(self, chars):
        write = 0
        read = 0
        
        while read < len(chars):
            char = chars[read]
            count = 0
            
            # Count the number of occurrences of the current character
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1
            
            # Write the character
            chars[write] = char
            write += 1
            
            # Write the count if greater than 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        
        return write

# Example usage:
solution = Solution()
chars1 = ["a","a","b","b","c","c","c"]
length1 = solution.compress(chars1)
print(length1)  # Output: 6
print(chars1[:length1])  # Output: ["a","2","b","2","c","3"]

chars2 = ["a"]
length2 = solution.compress(chars2)
print(length2)  # Output: 1
print(chars2[:length2])  # Output: ["a"]

chars3 = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
length3 = solution.compress(chars3)
print(length3)  # Output: 4
print(chars3[:length3])  # Output: ["a","b","1","2"]
