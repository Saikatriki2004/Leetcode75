from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n  # Initialize the answer array with 0s
        stack = []  # This will store indices of the temperatures array

        for i in range(n):
            # While the stack is not empty and the current temperature is greater
            # than the temperature at the index stored in the stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()  # Get the index of the temperature to update
                answer[idx] = i - idx  # Calculate the number of days to wait
            
            # Push the current index onto the stack
            stack.append(i)
        
        return answer

# Example usage
solution = Solution()
temperatures = [73,74,75,71,69,72,76,73]
print(solution.dailyTemperatures(temperatures))  # Output: [1,1,4,2,1,1,0,0]

temperatures = [30,40,50,60]
print(solution.dailyTemperatures(temperatures))  # Output: [1,1,1,0]

temperatures = [30,60,90]
print(solution.dailyTemperatures(temperatures))  # Output: [1,1,0]
