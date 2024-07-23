class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        left = 0
        zero_count = 0
        max_length = 0
        
        for right in range(len(nums)):
            # Expand the window by moving the right pointer
            if nums[right] == 0:
                zero_count += 1
            
            # If there are more than one zeroes, shrink the window from the left
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            # Update max_length considering that we can delete one element
            max_length = max(max_length, right - left)
        
        # If the array consists only of 1's, we need to remove one element, so the length will be reduced by 1
        if max_length == len(nums):
            return max_length - 1
        
        return max_length
# Create an instance of the Solution class
solution = Solution()

# Example 1
nums1 = [1,1,0,1]
print(solution.longestSubarray(nums1))  # Output: 3

# Example 2
nums2 = [0,1,1,1,0,1,1,0,1]
print(solution.longestSubarray(nums2))  # Output: 5

# Example 3
nums3 = [1,1,1]
print(solution.longestSubarray(nums3))  # Output: 2
