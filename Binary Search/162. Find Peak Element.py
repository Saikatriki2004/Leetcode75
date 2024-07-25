class Solution:
    def findPeakElement(self, nums):
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Check if mid is a peak element
            if (mid == 0 or nums[mid] > nums[mid - 1]) and (mid == len(nums) - 1 or nums[mid] > nums[mid + 1]):
                return mid
            
            # If the element to the left is greater, move left
            if mid > 0 and nums[mid] < nums[mid - 1]:
                right = mid - 1
            # If the element to the right is greater, move right
            else:
                left = mid + 1
        
        # This return is just a fallback. The loop should always return a peak index.
        return -1

# Example usage
solution = Solution()
print(solution.findPeakElement([1, 2, 3, 1]))  # Output: 2
print(solution.findPeakElement([1, 2, 1, 3, 5, 6, 4]))  # Output: 5 (or another peak index)
