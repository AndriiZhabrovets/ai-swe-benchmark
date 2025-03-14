class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    dummy = ListNode()  # Create a dummy node to simplify the merging process
    current = dummy  # This pointer will be used to build the new list

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1  # Link current node to list1 node
            list1 = list1.next  # Move to the next node in list1
        else:
            current.next = list2  # Link current node to list2 node
            list2 = list2.next  # Move to the next node in list2
        current = current.next  # Move the current pointer to the next node

    # At this point, at least one of the lists is exhausted. Link the remaining nodes.
    if list1:
        current.next = list1
    elif list2:
        current.next = list2

    return dummy.next  # Return the merged list starting from the next of dummy