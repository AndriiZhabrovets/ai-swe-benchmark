import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    # Create a min heap
    min_heap = []
    
    # Initialize the heap with the head of each list
    for idx, l in enumerate(lists):
        if l is not None:
            heapq.heappush(min_heap, (l.val, idx, l))
    
    # Create a dummy node to help with the merging process
    dummy = ListNode(0)
    current = dummy
    
    while min_heap:
        # Get the smallest node from the heap
        val, idx, node = heapq.heappop(min_heap)
        current.next = node  # Link the smallest node to the merged list
        current = current.next  # Move the current pointer
        
        # If there is a next node in the same list, push it to the heap
        if node.next is not None:
            heapq.heappush(min_heap, (node.next.val, idx, node.next))
    
    # Return the merged list, which is next to the dummy node
    return dummy.next