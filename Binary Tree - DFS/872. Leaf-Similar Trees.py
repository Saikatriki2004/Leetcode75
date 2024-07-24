class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def getLeafSequence(root: TreeNode):
            """Helper function to get the leaf sequence of a tree."""
            leaves = []
            def dfs(node: TreeNode):
                if node:
                    if not node.left and not node.right:  # It's a leaf node
                        leaves.append(node.val)
                    if node.left:
                        dfs(node.left)
                    if node.right:
                        dfs(node.right)
            dfs(root)
            return leaves
        
        # Get leaf sequences for both trees
        leaves1 = getLeafSequence(root1)
        leaves2 = getLeafSequence(root2)
        
        # Compare the two leaf sequences
        return leaves1 == leaves2
# Creating two binary trees for testing
root1 = TreeNode(3)
root1.left = TreeNode(5)
root1.right = TreeNode(1)
root1.left.left = TreeNode(6)
root1.left.right = TreeNode(2)
root1.left.right.left = TreeNode(7)
root1.left.right.right = TreeNode(4)
root1.right.right = TreeNode(8)

root2 = TreeNode(3)
root2.left = TreeNode(5)
root2.right = TreeNode(1)
root2.left.left = TreeNode(6)
root2.left.right = TreeNode(7)
root2.right.left = TreeNode(4)
root2.right.right = TreeNode(2)
root2.right.right.left = TreeNode(9)
root2.right.right.right = TreeNode(8)

solution = Solution()
print(solution.leafSimilar(root1, root2))  # Output: True
