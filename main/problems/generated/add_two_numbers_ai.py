from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0

    while l1 is not None or l2 is not None or carry:
        val1 = l1.val if l1 is not None else 0
        val2 = l2.val if l2 is not None else 0
        
        # Calculate sum of current digits plus carry
        total = val1 + val2 + carry
        carry = total // 10  # Update carry for next iteration
        current.next = ListNode(total % 10)  # Create a new node for the digit
        current = current.next  # Move to the next node
        
        # Move to the next nodes in the input lists, if available
        if l1 is not None:
            l1 = l1.next
        if l2 is not None:
            l2 = l2.next

    return dummy_head.next  # Return the next of dummy head to skip the initial zero