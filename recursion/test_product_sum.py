from product_sum import productSum


def testProductSum():
    assert productSum([1, [2, [3]]]) == 23
    assert productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]) == 12
    assert productSum([1, 1, 1, 1, 1]) == 5
    assert productSum([1, 2, 3, [4]]) == 14
