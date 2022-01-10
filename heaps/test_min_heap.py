from min_heap import MinHeap

def testMinHeap():
    array = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]
    heap = MinHeap(array)
    assert heap.peek() == -5
    heap.remove()
    assert heap.peek() == 2
    heap.remove()
    heap.remove()
    heap.remove()
    heap.remove()
    heap.remove()
    heap.remove()
    array = [991, -731, -882, 100, 280, -43, 432, 771, -581, 180, -382, -998, 847, 80, -220, 680, 769, -75, -817, 366, 956, 749, 471, 228, -435, -269, 652, -331, -387, -657, -255, 382, -216, -6, -163, -681, 980, 913, -169, 972, -523, 354, 747, 805, 382, -827, -796, 372, 753, 519, 906] 
    heap = MinHeap(array)
    heap.remove()
    heap.remove()
    heap.remove()
    heap.remove()
    heap.remove()