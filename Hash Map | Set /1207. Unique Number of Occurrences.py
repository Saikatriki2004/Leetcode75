class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        from collections import Counter
        
        # Step 1: Count occurrences of each number
        count = Counter(arr)
        
        # Step 2: Get the frequencies of counts
        frequencies = list(count.values())
        
        # Step 3: Check if frequencies are unique
        return len(frequencies) == len(set(frequencies))
# Create an instance of the Solution class
solution = Solution()

# Example 1
arr1 = [1, 2, 2, 1, 1, 3]
print(solution.uniqueOccurrences(arr1))  # Output: True

# Example 2
arr2 = [1, 2]
print(solution.uniqueOccurrences(arr2))  # Output: False

# Example 3
arr3 = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
print(solution.uniqueOccurrences(arr3))  # Output: True
