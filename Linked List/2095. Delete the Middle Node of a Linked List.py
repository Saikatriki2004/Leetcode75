class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            # If the list is empty or has only one node, return None
            return None
        
        # Step 1: Find the length of the linked list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        # The middle index to remove
        middle_index = length // 2
        
        # Step 2: Delete the middle node
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head
        
        for _ in range(middle_index):
            prev = current
            current = current.next
        
        # Remove the middle node
        prev.next = current.next
        
        return dummy.next

# Helper function to print the linked list
def printList(head: ListNode):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage:
# Creating a linked list: 1 -> 3 -> 4 -> 7 -> 1 -> 2 -> 6
head = ListNode(1, ListNode(3, ListNode(4, ListNode(7, ListNode(1, ListNode(2, ListNode(6))))))))
solution = Solution()
new_head = solution.deleteMiddle(head)
printList(new_head)  # Output should be: 1 -> 3 -> 4 -> 1 -> 2 -> 6
