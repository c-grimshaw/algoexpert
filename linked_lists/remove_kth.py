"""AlgoExpert - Linked Lists

The removal should be done in-place, which means the original
data structure should be mutated.

You can assume that the input list will always have at least k nodes.
"""

from linked_lists.linked_list import LinkedList


def remove_kth_node(head: LinkedList, k: int):
    """Removes the kth node from the end of the list, in-place.

    Args:
        head (LinkedList): The head of the linked list.
        k (int): The distance from the last node of the linked list.
    """
    fast = slow = head
    counter = 1
    while counter <= k:
        fast = fast.next
        counter += 1

    # If the head is being removed, mutate the head
    if fast is None:
        head.value = head.next.value
        head.next = head.next.next
        return

    # Else, walk down and remove the node
    while fast.next is not None:
        slow, fast = slow.next, fast.next
    slow.next = slow.next.next
