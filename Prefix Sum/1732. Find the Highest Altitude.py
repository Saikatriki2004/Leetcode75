class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        current_altitude = 0
        max_altitude = 0
        
        for g in gain:
            current_altitude += g
            max_altitude = max(max_altitude, current_altitude)
        
        return max_altitude
# Create an instance of the Solution class
solution = Solution()

# Example 1
gain1 = [-5,1,5,0,-7]
print(solution.largestAltitude(gain1))  # Output: 1

# Example 2
gain2 = [-4,-3,-2,-1,4,3,2]
print(solution.largestAltitude(gain2))  # Output: 0
