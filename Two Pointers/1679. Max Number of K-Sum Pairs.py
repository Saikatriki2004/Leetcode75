from collections import Counter

class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        count = Counter(nums)
        operations = 0

        for num in list(count):
            complement = k - num
            
            if complement in count:
                if num == complement:
                    # Special case where num == complement (i.e., k is even and num == k / 2)
                    operations += count[num] // 2
                else:
                    # Calculate the number of pairs we can make with num and complement
                    pairs = min(count[num], count[complement])
                    operations += pairs
                    # Remove pairs from the count
                    count[num] -= pairs
                    count[complement] -= pairs
        
        return operations

# Example usage:
solution = Solution()
print(solution.maxOperations([1,2,3,4], 5))  # Output: 2
print(solution.maxOperations([3,1,3,4,3], 6))  # Output: 1
