class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0
    
    while l1 or l2 or carry:
        val1 = (l1.val if l1 else 0)
        val2 = (l2.val if l2 else 0)
        
        # Calculate the sum of the values and the carry
        total = val1 + val2 + carry
        carry = total // 10
        current.next = ListNode(total % 10)
        
        # Move to the next nodes
        current = current.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    
    return dummy_head.next