class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        
        # Check each bit position
        for bit in range(32):  # Assuming 32-bit integers
            bit_mask = 1 << bit
            a_bit = a & bit_mask
            b_bit = b & bit_mask
            c_bit = c & bit_mask
            
            if c_bit == 0:
                # If c's bit is 0, we need both a's and b's bits to be 0
                if a_bit != 0 and b_bit != 0:
                    flips += 2  # Both need to be flipped
                elif a_bit != 0 or b_bit != 0:
                    flips += 1  # Only one needs to be flipped
            else:
                # If c's bit is 1, we need at least one of a's or b's bits to be 1
                if a_bit == 0 and b_bit == 0:
                    flips += 1  # At least one needs to be flipped
        
        return flips

# Example usage
solution = Solution()
print(solution.minFlips(2, 6, 5))  # Output: 3
print(solution.minFlips(4, 2, 7))  # Output: 1
print(solution.minFlips(1, 2, 3))  # Output: 0
