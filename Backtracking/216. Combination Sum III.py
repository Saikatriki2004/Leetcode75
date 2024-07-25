class Solution:
    def combinationSum3(self, k, n):
        def backtrack(start, k, n, path, result):
            # Base case
            if len(path) == k:
                if sum(path) == n:
                    result.append(path[:])
                return
            
            # Recursion and pruning
            for i in range(start, 10):
                if sum(path) + i > n:  # If adding this number exceeds n, break
                    break
                path.append(i)
                backtrack(i + 1, k, n, path, result)
                path.pop()  # Remove last number to backtrack
        
        result = []
        backtrack(1, k, n, [], result)
        return result

# Example usage
solution = Solution()
print(solution.combinationSum3(3, 7))  # Output: [[1, 2, 4]]
print(solution.combinationSum3(3, 9))  # Output: [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
print(solution.combinationSum3(4, 1))  # Output: []
