class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: ListNode) -> int:
        # Step 1: Find the middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the list
        second_half = self.reverseList(slow)
        first_half = head
        
        # Step 3: Compute the maximum twin sum
        max_twin_sum = 0
        while second_half:
            max_twin_sum = max(max_twin_sum, first_half.val + second_half.val)
            first_half = first_half.next
            second_half = second_half.next
        
        return max_twin_sum
    
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

# Helper function to create and print a linked list from a list of values
def createLinkedList(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Example usage:
# Creating a linked list: 5 -> 4 -> 2 -> 1
head = createLinkedList([5, 4, 2, 1])
solution = Solution()
print(solution.pairSum(head))  # Output should be 6
