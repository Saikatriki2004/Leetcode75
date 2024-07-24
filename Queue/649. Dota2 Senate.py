from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant_queue = deque()
        dire_queue = deque()
        
        # Initialize the queues with the indices of each senator
        for i, s in enumerate(senate):
            if s == 'R':
                radiant_queue.append(i)
            else:
                dire_queue.append(i)
        
        # Simulate the voting process
        while radiant_queue and dire_queue:
            # Get the indices of the current senators
            radiant_index = radiant_queue.popleft()
            dire_index = dire_queue.popleft()
            
            if radiant_index < dire_index:
                # Radiant bans Dire, add Radiant senator back to the queue
                radiant_queue.append(radiant_index + len(senate))
            else:
                # Dire bans Radiant, add Dire senator back to the queue
                dire_queue.append(dire_index + len(senate))
        
        # Determine the winner
        return "Radiant" if radiant_queue else "Dire"

# Example usage:
solution = Solution()
print(solution.predictPartyVictory("RD"))  # Output: "Radiant"
print(solution.predictPartyVictory("RDD")) # Output: "Dire"
