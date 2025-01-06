from typing import List, Optional
import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    for i in range(len(lists)):
        lists[i] = list_to_linked_list(lists[i])
    ListNode.__lt__ = lambda self, other: self.val < other.val
    h = []
    head = tail = ListNode(0)
    for i in lists:
        if i: heapq.heappush(h, i)
    while h:
        node = heapq.heappop(h)
        tail.next = node
        tail = tail.next
        if node.next: heapq.heappush(h, node.next)
    return linked_list_to_list(head.next)

def list_to_linked_list(lst: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    cur = dummy
    for val in lst:
        cur.next = ListNode(val)
        cur = cur.next
    return dummy.next

def linked_list_to_list(node: Optional[ListNode]) -> List[int]:
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


