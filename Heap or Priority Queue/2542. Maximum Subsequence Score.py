import heapq

class Solution:
    def maxScore(self, nums1, nums2, k):
        # Pair the elements of nums1 and nums2 and sort by nums2 in descending order
        paired = sorted(zip(nums1, nums2), key=lambda x: -x[1])
        
        max_score = 0
        current_sum = 0
        min_heap = []
        
        for num1, num2 in paired:
            # Add the current num1 to the min-heap and current sum
            heapq.heappush(min_heap, num1)
            current_sum += num1
            
            # If we have more than k elements in the heap, remove the smallest
            if len(min_heap) > k:
                current_sum -= heapq.heappop(min_heap)
            
            # If we have exactly k elements, calculate the score
            if len(min_heap) == k:
                max_score = max(max_score, current_sum * num2)
        
        return max_score

# Example usage
solution = Solution()
print(solution.maxScore([1,3,3,2], [2,1,3,4], 3))  # Output: 12
print(solution.maxScore([4,2,3,1,1], [7,5,10,9,6], 1))  # Output: 30
