"""AlgoExpert - Linked Lists"""

from dataclasses import dataclass


@dataclass
class LinkedList:
    """Base class for Linked List implementation."""

    def __init__(self, value):
        self.value = value
        self.next = None
