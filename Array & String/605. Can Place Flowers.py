class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        count = 0
        i = 0
        length = len(flowerbed)

        while i < length:
            if flowerbed[i] == 0:
                # Check if the current position and adjacent positions are empty or out of bounds
                if (i == 0 or flowerbed[i - 1] == 0) and (i == length - 1 or flowerbed[i + 1] == 0):
                    # Plant a flower here
                    flowerbed[i] = 1
                    count += 1
            i += 1

        return count >= n

# Example usage:
solution = Solution()
print(solution.canPlaceFlowers([1,0,0,0,1], 1))  # Output: True
print(solution.canPlaceFlowers([1,0,0,0,1], 2))  # Output: False
