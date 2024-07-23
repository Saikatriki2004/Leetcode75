class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # Calculate the sum of the first window
        current_sum = sum(nums[:k])
        max_sum = current_sum
        
        # Slide the window from left to right
        for i in range(k, len(nums)):
            # Update the window sum by adding the new element and removing the old element
            current_sum += nums[i] - nums[i - k]
            # Update the maximum sum if the current sum is greater
            max_sum = max(max_sum, current_sum)
        
        # Calculate the maximum average
        max_average = max_sum / k
        return max_average# Create an instance of the Solution class
solution = Solution()

# Example 1
nums1 = [1, 12, -5, -6, 50, 3]
k1 = 4
print(solution.findMaxAverage(nums1, k1))  # Output: 12.75000

# Example 2
nums2 = [5]
k2 = 1
print(solution.findMaxAverage(nums2, k2))  # Output: 5.00000

