def largestRange(array: list[int]) -> list[int]:
    seen = {num: True for num in array}
    largestRangeLength = 0
    largestRangePair = [None, None]
    for i in array:
        if not seen[i]:
            continue

        # Range of a single letter is always 1
        currentRange = 1
        left = right = i
        while seen.get(left-1, False):
            seen[left] = False
            left -= 1
        while seen.get(right+1, False):
            seen[right] = False
            right += 1

        currentRange = abs(right-left+1)

        if currentRange > largestRangeLength:
            largestRangeLength = currentRange
            largestRangePair = [left, right]

    return largestRangePair