class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        # Initialize pointers for odd and even lists
        odd_head = head
        even_head = head.next
        odd = odd_head
        even = even_head
        
        # Traverse and separate odd and even nodes
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        
        # Connect the end of the odd list to the head of the even list
        odd.next = even_head
        
        return odd_head

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
new_head = solution.oddEvenList(head)
printList(new_head)  # Output should be: 1 -> 3 -> 5 -> 2 -> 4
