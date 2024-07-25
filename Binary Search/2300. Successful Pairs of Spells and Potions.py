from bisect import bisect_left

class Solution:
    def successfulPairs(self, spells, potions, success):
        # Sort potions to enable binary search
        potions.sort()
        
        result = []
        
        # For each spell, calculate the number of successful pairs
        for spell in spells:
            # Calculate the minimum potion strength needed for a successful pair
            min_potion_strength = (success + spell - 1) // spell  # Equivalent to ceil(success / spell)
            
            # Find the index of the first potion that meets the requirement
            index = bisect_left(potions, min_potion_strength)
            
            # Number of successful pairs is the number of potions from this index to the end
            successful_pairs_count = len(potions) - index
            result.append(successful_pairs_count)
        
        return result

# Example usage
solution = Solution()
spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7
print(solution.successfulPairs(spells, potions, success))  # Output: [4, 0, 3]

spells = [3,1,2]
potions = [8,5,8]
success = 16
print(solution.successfulPairs(spells, potions, success))  # Output: [2, 0, 2]
