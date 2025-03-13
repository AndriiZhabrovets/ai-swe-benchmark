import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    # Create a min-heap
    min_heap = []
    
    # Initialize the heap with the head of each linked list
    for i, l in enumerate(lists):
        if l:
            heapq.heappush(min_heap, (l.val, i, l))  # (node value, index of list, node)
    
    # Create a dummy head for the merged linked list
    dummy = ListNode(0)
    current = dummy
    
    while min_heap:
        # Get the smallest node from the heap
        val, index, node = heapq.heappop(min_heap)
        current.next = ListNode(val)  # Add the smallest node to the merged list
        current = current.next  # Move the current pointer
        
        # If there is a next node in the same list, push it to the heap
        if node.next:
            heapq.heappush(min_heap, (node.next.val, index, node.next))
    
    return dummy.next  # Return the merged linked list starting from the next of dummy