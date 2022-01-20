"""AlgoExpert - Linked Lists

The removal should be done in-place, which means the original
data structure should be mutated. The function should return the new head.

You can assume that the input list will always have at least k nodes.
"""

from linked_lists.linked_list import LinkedList


def shift_list(head: LinkedList, k: int):
    """Shift a singly linked list in-place by k positions, and return
    the new head.

    Args:
        head (LinkedList): The head of the linked list.
        k (int): The number of positions to shift (+/-)
    """
    num_nodes, tail = 1, head
    while tail.next:
        tail = tail.next
        num_nodes += 1

    shift = k % num_nodes

    if shift == 0:
        return head

    new_tail = head
    for _ in range(num_nodes - shift - 1):
        new_tail = new_tail.next
    new_head = new_tail.next

    new_tail.next = None
    tail.next = head

    return new_head
