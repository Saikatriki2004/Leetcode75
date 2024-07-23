class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        # Convert lists to sets to remove duplicates and allow efficient operations
        set1 = set(nums1)
        set2 = set(nums2)
        
        # Compute the difference
        diff1 = set1 - set2
        diff2 = set2 - set1
        
        # Convert the results to lists
        return [list(diff1), list(diff2)]
# Create an instance of the Solution class
solution = Solution()

# Example 1
nums1 = [1, 2, 3]
nums2 = [2, 4, 6]
print(solution.findDifference(nums1, nums2))  # Output: [[1, 3], [4, 6]]

# Example 2
nums1 = [1, 2, 3, 3]
nums2 = [1, 1, 2, 2]
print(solution.findDifference(nums1, nums2))  # Output: [[3], []]
