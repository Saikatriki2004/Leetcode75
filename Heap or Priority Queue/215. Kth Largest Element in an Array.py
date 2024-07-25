import heapq

class Solution:
    def findKthLargest(self, nums, k):
        # Initialize a min-heap
        min_heap = []
        
        # Iterate over all elements in the array
        for num in nums:
            # Add the element to the heap
            heapq.heappush(min_heap, num)
            
            # If the heap size exceeds k, remove the smallest element
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        # The root of the heap is the k-th largest element
        return min_heap[0]

# Example usage:
sol = Solution()
nums1 = [3,2,1,5,6,4]
k1 = 2
print(sol.findKthLargest(nums1, k1))  # Output: 5

nums2 = [3,2,3,1,2,4,5,5,6]
k2 = 4
print(sol.findKthLargest(nums2, k2))  # Output: 4
