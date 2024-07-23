class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        
        for i, num in enumerate(nums):
            # Compute right sum
            right_sum = total_sum - left_sum - num
            
            # Check if left sum equals right sum
            if left_sum == right_sum:
                return i
            
            # Update left sum for the next iteration
            left_sum += num
        
        return -1
# Create an instance of the Solution class
solution = Solution()

# Example 1
nums1 = [1, 7, 3, 6, 5, 6]
print(solution.pivotIndex(nums1))  # Output: 3

# Example 2
nums2 = [1, 2, 3]
print(solution.pivotIndex(nums2))  # Output: -1

# Example 3
nums3 = [2, 1, -1]
print(solution.pivotIndex(nums3))  # Output: 0
