class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    dummy = ListNode(0)  # Create a dummy node to simplify the merge process
    current = dummy  # Pointer to build the new list

    # While both lists have nodes to compare
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1  # Link to the smaller node
            list1 = list1.next  # Move to the next node in list1
        else:
            current.next = list2  # Link to the smaller node
            list2 = list2.next  # Move to the next node in list2
        current = current.next  # Move the current pointer

    # If there are remaining nodes in either list, link them
    if list1:
        current.next = list1
    elif list2:
        current.next = list2

    return dummy.next  # Return the merged list, which starts from dummy.next