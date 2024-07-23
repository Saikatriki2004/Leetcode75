class Solution:
    def moveZeroes(self, nums):
        last_non_zero_index = 0  # Pointer to place the next non-zero element
        
        # Traverse the array
        for current_index in range(len(nums)):
            if nums[current_index] != 0:
                # Swap non-zero element with the element at last_non_zero_index
                nums[last_non_zero_index], nums[current_index] = nums[current_index], nums[last_non_zero_index]
                last_non_zero_index += 1
        
        # The remaining part of the array will be filled with zeros
        # We don't need to explicitly set zeros as they are already in place due to the swaps

# Example usage:
solution = Solution()
nums1 = [0,1,0,3,12]
solution.moveZeroes(nums1)
print(nums1)  # Output: [1, 3, 12, 0, 0]

nums2 = [0]
solution.moveZeroes(nums2)
print(nums2)  # Output: [0]
