class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        # Base case: If the root is None or the root's value is the target
        if root is None or root.val == val:
            return root
        
        # Recursive case: If the target value is less than the root's value,
        # search in the left subtree
        if val < root.val:
            return self.searchBST(root.left, val)
        
        # Recursive case: If the target value is greater than the root's value,
        # search in the right subtree
        return self.searchBST(root.right, val)

# Example usage:
# Creating a binary search tree for testing
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

solution = Solution()
result = solution.searchBST(root, 2)  # Output: [2,1,3]

# Helper function to print tree
def print_tree(node):
    if node is None:
        return "[]"
    result = []
    queue = [node]
    while queue:
        current = queue.pop(0)
        if current:
            result.append(current.val)
            queue.append(current.left)
            queue.append(current.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result

print(print_tree(result))  # Output: [2, 1, 3]

result = solution.searchBST(root, 5)  # Output: []
print(print_tree(result))  # Output: []
