class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        
        # Find the node to be deleted
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node to be deleted is found
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            # Node with two children
            min_larger_node = self.findMin(root.right)
            root.val = min_larger_node.val
            root.right = self.deleteNode(root.right, min_larger_node.val)
        
        return root
    
    def findMin(self, node: TreeNode) -> TreeNode:
        while node.left:
            node = node.left
        return node

# Example usage:
# Creating a binary search tree for testing
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)

solution = Solution()
result = solution.deleteNode(root, 3)  # Output: [5,4,6,2,null,null,7]

# Helper function to print tree in level-order
def print_tree(root):
    if not root:
        return "[]"
    result = []
    queue = [root]
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

print(print_tree(result))  # Output: [5, 4, 6, 2, None, None, 7]
