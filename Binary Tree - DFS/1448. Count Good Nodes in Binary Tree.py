class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, max_val: int) -> int:
            if not node:
                return 0
            
            # Check if the current node is good
            good = 1 if node.val >= max_val else 0
            
            # Update the maximum value on the path
            max_val = max(max_val, node.val)
            
            # Continue DFS traversal for left and right children
            good += dfs(node.left, max_val)
            good += dfs(node.right, max_val)
            
            return good
        
        # Start DFS traversal with initial maximum value as negative infinity
        return dfs(root, float('-inf'))
# Creating a binary tree for testing
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.left = TreeNode(3)
root.right.right = TreeNode(5)

solution = Solution()
print(solution.goodNodes(root))  # Output: 4
