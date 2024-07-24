class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        def dfs(node, direction, length):
            nonlocal max_length
            if not node:
                return
            
            # Update the maximum length found so far
            max_length = max(max_length, length)
            
            # If the direction is right, move to the left child
            if direction == "right":
                dfs(node.left, "left", length + 1)
                dfs(node.right, "right", 1)  # Reset length if direction changes to right
            # If the direction is left, move to the right child
            else:
                dfs(node.right, "right", length + 1)
                dfs(node.left, "left", 1)  # Reset length if direction changes to left
        
        max_length = 0
        # Start DFS from root, considering both initial directions
        dfs(root, "right", 0)
        dfs(root, "left", 0)
        
        return max_length
# Example usage:
# Creating a binary tree for testing
root = TreeNode(1)
root.right = TreeNode(1)
root.right.left = TreeNode(1)
root.right.left.right = TreeNode(1)
root.right.left.right.left = TreeNode(1)

solution = Solution()
print(solution.longestZigZag(root))  # Output: 3
