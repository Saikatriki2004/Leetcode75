from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        if not root:
            return []

        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            
            for i in range(level_size):
                node = queue.popleft()
                
                # If it's the last node in this level, add it to the result
                if i == level_size - 1:
                    result.append(node.val)
                
                # Add child nodes of the current node to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result

# Example usage:
# Creating a binary tree for testing
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)

solution = Solution()
print(solution.rightSideView(root))  # Output: [1, 3, 4]
