class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        zero_count = 0
        max_length = 0
        
        for right in range(len(nums)):
            # If the current element is 0, increment the zero_count
            if nums[right] == 0:
                zero_count += 1
            
            # While the number of zeros exceeds k, shrink the window from the left
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            # Create an instance of the Solution class
solution = Solution()

# Example 1
nums1 = [1,1,1,0,0,0,1,1,1,1,0]
k1 = 2
print(solution.longestOnes(nums1, k1))  # Output: 6

# Example 2
nums2 = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k2 = 3
print(solution.longestOnes(nums2, k2))  # Output: 10

            # Update max_length with the current window size
            max_length = max(max_length, right - left + 1)
        
        return max_length
