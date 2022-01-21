"""AlgoExpert - Heaps

Not an AlgoExpert challenge, but an implementation of a
MaxHeap using built-ins.
"""

import heapq


class MaxHeap:
    """MaxHeap implementation."""

    _heap: list

    def __init__(self):
        self._heap = []

    def insert(self, value):
        """Insert a value into the heap, preserving heap invariant."""
        heapq.heappush(self._heap, -1 * value)

    def peek(self):
        """Returns the value of the maximum element in the heap."""
        return -1 * self._heap[0]

    def pop(self):
        """Returns the maximum element in the heap, removing it."""
        return -1 * heapq.heappop(self._heap)

    def __len__(self):
        return len(self._heap)
