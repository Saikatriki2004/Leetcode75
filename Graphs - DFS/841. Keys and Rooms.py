from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms):
        n = len(rooms)
        visited = set()
        queue = deque([0])
        
        while queue:
            room = queue.popleft()
            if room not in visited:
                visited.add(room)
                for key in rooms[room]:
                    if key not in visited:
                        queue.append(key)
        
        return len(visited) == n

# Example usage:
# Initialize the Solution object
solution = Solution()
print(solution.canVisitAllRooms([[1], [2], [3], []]))  # Output: True
print(solution.canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]))  # Output: False
