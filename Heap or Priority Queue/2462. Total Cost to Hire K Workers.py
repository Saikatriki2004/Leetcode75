import heapq

class Solution:
    def totalCost(self, costs, k, candidates):
        n = len(costs)
        
        if candidates * 2 >= n:
            # If the number of candidates considered from both ends exceed the list length, we just take the smallest k elements.
            return sum(heapq.nsmallest(k, costs))
        
        left_heap = []
        right_heap = []
        
        # Add initial candidates to the heaps
        for i in range(candidates):
            heapq.heappush(left_heap, (costs[i], i))
        for j in range(n - candidates, n):
            heapq.heappush(right_heap, (costs[j], j))
        
        total_cost = 0
        hired_count = 0
        left_index = candidates
        right_index = n - candidates - 1
        
        while hired_count < k:
            # Get the smallest element from both heaps
            if left_heap and (not right_heap or left_heap[0][0] <= right_heap[0][0]):
                cost, idx = heapq.heappop(left_heap)
                total_cost += cost
                hired_count += 1
                # Add new candidate to the left heap if available
                if left_index <= right_index:
                    heapq.heappush(left_heap, (costs[left_index], left_index))
                    left_index += 1
            else:
                cost, idx = heapq.heappop(right_heap)
                total_cost += cost
                hired_count += 1
                # Add new candidate to the right heap if available
                if right_index >= left_index:
                    heapq.heappush(right_heap, (costs[right_index], right_index))
                    right_index -= 1
        
        return total_cost

# Example usage
solution = Solution()
print(solution.totalCost([17,12,10,2,7,2,11,20,8], 3, 4))  # Output: 11
print(solution.totalCost([1,2,4,1], 3, 3))  # Output: 4
print(solution.totalCost([4866,4857,4378,4876,3594,4874,4717,4680,4813,4938,4156,4724], 9, 2))  # Output: 40785


# Example usage
solution = Solution()
print(solution.totalCost([17,12,10,2,7,2,11,20,8], 3, 4))  # Output: 11
print(solution.totalCost([1,2,4,1], 3, 3))  # Output: 4
