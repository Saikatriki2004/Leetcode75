class Solution:
    def productExceptSelf(self, nums):
        length = len(nums)
        result = [1] * length
        
        # Step 1: Calculate prefix products
        prefix_product = 1
        for i in range(length):
            result[i] = prefix_product
            prefix_product *= nums[i]
        
        # Step 2: Calculate suffix products and update the result
        suffix_product = 1
        for i in range(length - 1, -1, -1):
            result[i] *= suffix_product
            suffix_product *= nums[i]
        
        return result

# Example usage:
solution = Solution()
print(solution.productExceptSelf([1,2,3,4]))      # Output: [24, 12, 8, 6]
print(solution.productExceptSelf([-1,1,0,-3,3]))  # Output: [0, 0, 9, 0, 0]
