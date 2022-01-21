"""AlgoExpert - Heap Tests"""
from heaps.min_heap import MinHeap
from heaps.max_heap import MaxHeap
from heaps.continuous_median import ContinuousMedianHandler


def test_min_heap():
    """MinHeap tests."""
    heap = MinHeap()
    for i in range(0, 11):
        heap.insert(i)
    assert heap.peek() == 0
    assert heap.pop() == 0
    assert heap.peek() == 1


def test_max_heap():
    """MaxHeap tests."""
    heap = MaxHeap()
    for i in range(0, 11):
        heap.insert(i)
    assert heap.peek() == 10
    assert heap.pop() == 10
    assert heap.peek() == 9


def test_continuous_median():
    """Median Tests"""
    heap = ContinuousMedianHandler()
    values = [1, 3, 7]
    for value in values:
        heap.insert(value)

    assert heap.get_median() == 3
    heap.insert(8)

    assert heap.get_median() == 5
