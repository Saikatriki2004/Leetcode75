class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next  # Store the next node
            curr.next = prev       # Reverse the current node's pointer
            prev = curr            # Move prev to this node
            curr = next_node       # Move to the next node
        
        return prev  # prev will be the new head of the reversed list

# Helper function to print the linked list
def printList(head: ListNode):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage:
# Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
solution = Solution()
reversed_head = solution.reverseList(head)
printList(reversed_head)  # Output should be: 5 -> 4 -> 3 -> 2 -> 1
