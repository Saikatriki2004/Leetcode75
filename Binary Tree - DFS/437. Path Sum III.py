class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def dfs(node, current_sum):
            if not node:
                return 0
            
            # Calculate the current prefix sum
            current_sum += node.val
            
            # Count paths that end at the current node and have the required sum
            path_count = prefix_sum_count.get(current_sum - targetSum, 0)
            
            # Update the prefix sum count for the current path
            prefix_sum_count[current_sum] = prefix_sum_count.get(current_sum, 0) + 1
            
            # Recursively count paths in the left and right subtrees
            path_count += dfs(node.left, current_sum)
            path_count += dfs(node.right, current_sum)
            
            # Backtrack: Remove the current path sum count from the dictionary
            prefix_sum_count[current_sum] -= 1
            
            return path_count
        
        # Dictionary to store the prefix sums and their frequencies
        prefix_sum_count = {0: 1}
        
        # Start DFS traversal from the root
        return dfs(root, 0)
# Creating a binary tree for testing
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(-3)
root.left.left = TreeNode(3)
root.left.right = TreeNode(2)
root.right.right = TreeNode(11)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(-2)
root.left.right.right = TreeNode(1)

solution = Solution()
print(solution.pathSum(root, 8))  # Output: 3
