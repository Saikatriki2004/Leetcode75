class Solution:
    def tribonacci(self, n: int) -> int:
        # Base cases
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        
        # Initialize the first three values
        t0, t1, t2 = 0, 1, 1
        
        # Compute tribonacci values iteratively
        for _ in range(3, n + 1):
            t_next = t0 + t1 + t2
            t0, t1, t2 = t1, t2, t_next
        
        return t2

# Example usage
solution = Solution()
print(solution.tribonacci(4))  # Output: 4
print(solution.tribonacci(25)) # Output: 1389537
