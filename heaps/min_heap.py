# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        for i in range(0, len(array)):
            while i > 0 and array[i] < array[(parentIdx:= self.parent(i))]:
                # Swap the parent and child
                array[parentIdx], array[i] = array[i], array[parentIdx]

                # Update the index of the child
                i = parentIdx        
        return array

    def peek(self):
        return self.heap[0]

    def remove(self):
        # We only ever remove the root node
        removed = self.heap[0]
        self.heap[0] = self.heap.pop()

        trickleNodeIdx = 0
        while self.hasSmallerChild(trickleNodeIdx):
            smallerChildIdx = self.calculateSmallerChildIdx(trickleNodeIdx)

            self.heap[trickleNodeIdx], self.heap[smallerChildIdx] = self.heap[smallerChildIdx], self.heap[trickleNodeIdx]
            trickleNodeIdx = smallerChildIdx

        return removed


    def hasSmallerChild(self, idx):
        return self.left_child(idx) < len(self.heap) and self.heap[self.left_child(idx)] < self.heap[idx] or \
               self.right_child(idx) < len(self.heap) and self.heap[self.right_child(idx)] < self.heap[idx]

    
    def calculateSmallerChildIdx(self, idx):
        if self.right_child(idx) == len(self.heap):
            return self.left_child(idx)
        
        if self.heap[self.left_child(idx)] < self.heap[self.right_child(idx)]:
            return self.left_child(idx)
        else:
            return self.right_child(idx)


    def insert(self, value):
        # Turn value into last node by appending it at the end of the array
        self.heap.append(value)

        # Keep track of the last index of the new node
        newNodeIdx = len(self.heap) - 1

        # The following code executes the "trickle up" algorithm.

        # If the new node is not in the root position,
        # and it's less than its parent node:
        while newNodeIdx > 0 and self.heap[newNodeIdx] < self.heap[self.parent(newNodeIdx)]:
            # Swap the parent and child
            self.heap[self.parent(newNodeIdx)], self.heap[newNodeIdx] = self.heap[newNodeIdx], self.heap[self.parent(newNodeIdx)]

            # Update the index of the child
            newNodeIdx = self.parent(newNodeIdx)

    def left_child(self, idx):
        return (idx * 2) + 1
    
    def right_child(self, idx):
        return (idx * 2) + 2
    
    def parent(self, idx):
        return (idx - 1) // 2