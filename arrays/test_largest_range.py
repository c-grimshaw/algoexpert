from largest_range import largestRange

def testLargestRange():
    assert largestRange([1,11,3,0,15,5,2,4,10,7,12,6]) == [0, 7]
    assert largestRange([1]) == [1, 1]
    assert largestRange([1,1,1,1,3,4]) == [3,4]