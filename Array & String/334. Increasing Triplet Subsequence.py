class Solution:
    def increasingTriplet(self, nums):
        first_min = float('inf')
        second_min = float('inf')
        
        for num in nums:
            if num <= first_min:
                first_min = num
            elif num <= second_min:
                second_min = num
            else:
                # We found a num greater than both first_min and second_min
                return True
        
        return False

# Example usage:
solution = Solution()
print(solution.increasingTriplet([1,2,3,4,5]))      # Output: True
print(solution.increasingTriplet([5,4,3,2,1]))      # Output: False
print(solution.increasingTriplet([2,1,5,0,4,6]))    # Output: True
