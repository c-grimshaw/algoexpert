def maxSubsetSumNoAdjacent(array: list[int]) -> int:
    """Returns the maximum sub-array sum of non-adjacent elements in the array."""
    if len(array) == 0:
        return 0
    elif len(array) == 1:
        return array[0]

    maxSums = [0 for _ in range(0, len(array))]
    maxSums[0], maxSums[1] = array[0], max(array[0], array[1])

    for i in range(2, len(maxSums)):
        maxSums[i] = max(maxSums[i-2] + array[i], maxSums[i-1])
    
    return maxSums[-1]