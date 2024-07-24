class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Base case: if the root is null or if root is one of p or q
        if root is None or root == p or root == q:
            return root
        
        # Recursively find LCA in the left subtree
        left_lca = self.lowestCommonAncestor(root.left, p, q)
        # Recursively find LCA in the right subtree
        right_lca = self.lowestCommonAncestor(root.right, p, q)
        
        # If both left and right LCA are not null, the current root is the LCA
        if left_lca and right_lca:
            return root
        
        # If one of the LCA is null, return the non-null LCA
        return left_lca if left_lca else right_lca

# Example usage:
# Creating a binary tree for testing
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

p = root.left       # Node 5
q = root.right      # Node 1

solution = Solution()
lca = solution.lowestCommonAncestor(root, p, q)
print(lca.val)  # Output: 3
