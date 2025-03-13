import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    min_heap = []
    
    # Initialize the heap with the head of each list
    for i, l in enumerate(lists):
        if l:
            heapq.heappush(min_heap, (l.val, i, l))
    
    dummy = ListNode(0)
    current = dummy
    
    while min_heap:
        # Get the smallest node from the heap
        val, index, node = heapq.heappop(min_heap)
        current.next = node
        current = current.next
        
        # If there is a next node in the list, add it to the heap
        if node.next:
            heapq.heappush(min_heap, (node.next.val, index, node.next))
    
    return dummy.next