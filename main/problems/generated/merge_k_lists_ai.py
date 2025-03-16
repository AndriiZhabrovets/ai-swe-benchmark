import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    min_heap = []
    
    # Initialize the heap with the head nodes of each list
    for index, l in enumerate(lists):
        if l:
            heapq.heappush(min_heap, (l.val, index, l))
    
    # Create a dummy head for the merged list
    dummy = ListNode(0)
    current = dummy
    
    while min_heap:
        # Get the smallest element from the heap
        val, index, node = heapq.heappop(min_heap)
        current.next = ListNode(val)
        current = current.next
        
        # If there is a next node in the same list, push it to the heap
        if node.next:
            heapq.heappush(min_heap, (node.next.val, index, node.next))
    
    return dummy.next