"""AlgoExpert - Continuous Median - Heaps

A continuous median handler class that supports O(1) retrieval
of numbers inserted so far using the get_median() method.
"""

from heaps.max_heap import MaxHeap
from heaps.min_heap import MinHeap


class ContinuousMedianHandler:
    """A handler class supporting constant retrieval time of the median element"""

    lower: MaxHeap
    higher: MinHeap
    median: int

    def __init__(self):
        self.lower = MaxHeap()
        self.higher = MinHeap()
        self.median = None

    def update_median(self):
        """Updates the median of the instance."""
        if len(self.lower) == len(self.higher):
            self.median = (self.lower.peek() + self.higher.peek()) / 2
        else:
            longer = max(self.lower, self.higher, key=len)
            self.median = longer.peek()

    def rebalance(self):
        """Maintains the balance of the min/max properties."""
        if abs(len(self.lower) - len(self.higher)) <= 1:
            return
        shorter = min(self.lower, self.higher, key=len)
        longer = max(self.lower, self.higher, key=len)
        shorter.insert(longer.pop())

    def insert(self, value):
        """Inserts a value into the container.

        Args:
            value (int): Value to be inserted.
        """
        if len(self.lower) == 0 and len(self.higher) == 0:
            self.lower.insert(value)
        elif value < self.lower.peek():
            self.lower.insert(value)
        else:
            self.higher.insert(value)

        self.rebalance()
        self.update_median()

    def get_median(self):
        """Returns the median of the container."""
        return self.median
