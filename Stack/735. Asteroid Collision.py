class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for asteroid in asteroids:
            # Process collision only if current asteroid is moving left
            while stack and asteroid < 0 and stack[-1] > 0:
                top = stack[-1]
                if top < -asteroid:
                    stack.pop()  # The right-moving asteroid is smaller and explodes
                elif top == -asteroid:
                    stack.pop()  # Both asteroids are the same size and explode
                    break
                else:
                    break  # The left-moving asteroid is smaller and explodes
            else:
                stack.append(asteroid)  # No collision or moving right asteroid
        
        return stack
      # Create an instance of the Solution class
solution = Solution()

# Example 1
asteroids1 = [5,10,-5]
print(solution.asteroidCollision(asteroids1))  # Output: [5, 10]

# Example 2
asteroids2 = [8,-8]
print(solution.asteroidCollision(asteroids2))  # Output: []

# Example 3
asteroids3 = [10,2,-5]
print(solution.asteroidCollision(asteroids3))  # Output: [10]
