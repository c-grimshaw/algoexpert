"""AlgoExpert - Linked Lists Tests"""
import pytest
from linked_lists.linked_list import LinkedList
from linked_lists.remove_kth import remove_kth_node
from linked_lists.shift_list import shift_list


def list_matches_array(head: LinkedList, array: list):
    """Function for LL validation.

    Args:
        head (LinkedList): Head of LinkedList.
        array (list): Array to match.
    """
    i = 0
    while head and head.value == array[i]:
        i += 1
        head = head.next
    return i == len(array)


@pytest.fixture(name="head")
def linked_list():
    """Linked list fixture.

    0->1->2->3->4->5->6->7->8->9->X
    """
    head = cur = LinkedList(0)
    for i in range(1, 10):
        cur.next = LinkedList(i)
        cur = cur.next
    return head


def test_remove_kth_node(head):
    """Remove kth node tests."""
    assert list_matches_array(head, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    # Remove 4th node from end of list (value 6)
    remove_kth_node(head, 4)
    assert list_matches_array(head, [0, 1, 2, 3, 4, 5, 7, 8, 9])

    # Remove last node from end of list (value 9)
    remove_kth_node(head, 1)
    assert list_matches_array(head, [0, 1, 2, 3, 4, 5, 7, 8])

    # Remove first node from list (value 0)
    remove_kth_node(head, 8)
    assert list_matches_array(head, [1, 2, 3, 4, 5, 7, 8])


def test_shift_list(head):
    """Shift k positions tests."""

    # Shift five times to the right
    head = shift_list(head, 5)
    assert list_matches_array(head, [5, 6, 7, 8, 9, 0, 1, 2, 3, 4])

    # Shift five times to the left
    head = shift_list(head, -5)
    assert list_matches_array(head, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    # Shift single node
    head = LinkedList(1)
    head = shift_list(head, 5)
    assert list_matches_array(head, [1])
