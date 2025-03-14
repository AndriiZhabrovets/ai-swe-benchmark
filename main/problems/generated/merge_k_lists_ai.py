import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    min_heap = []
    
    # Initialize the heap with the head of each list
    for index, l in enumerate(lists):
        if l:
            heapq.heappush(min_heap, (l.val, index, l))
    
    # Dummy head for the result list
    head = ListNode(0)
    current = head
    
    while min_heap:
        # Get the smallest node from the heap
        val, index, node = heapq.heappop(min_heap)
        current.next = ListNode(val)  # Add the smallest node to the result
        current = current.next  # Move to the next position
        
        # If there's a next node in the list, add it to the heap
        if node.next:
            heapq.heappush(min_heap, (node.next.val, index, node.next))
    
    return head.next