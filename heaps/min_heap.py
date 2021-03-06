"""AlgoExpert - MinHeap - Heaps

Not an AlgoExpert challenge, but an implementation of a
MinHeap using built-ins.
"""

import heapq


class MinHeap:
    """MinHeap implementation."""

    _heap: list

    def __init__(self):
        self._heap = []

    def insert(self, value):
        """Insert a value into the heap, preserving heap invariant."""
        heapq.heappush(self._heap, value)

    def peek(self):
        """Returns the value of the maximum element in the heap."""
        return self._heap[0]

    def pop(self):
        """Returns the maximum element in the heap, removing it."""
        return heapq.heappop(self._heap)

    def __len__(self):
        """Length of heap."""
        return len(self._heap)
