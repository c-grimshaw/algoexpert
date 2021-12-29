def longestPeak(array: list[int]) -> int:
    """A peak is defined as:
    
    Strictly increasing until they reach a tip, at which point they become strictly decreasing.
    At least three integers are required to form a peak.
    """

    # Sliding window of three... when peak found, slide edges outward
    if len(array) < 3:
        return 0

    largestPeak = 0
    middleIdx = 1
    while middleIdx < len(array) - 1:
        peakFound = False

        leftIdx = middleIdx-1
        rightIdx = middleIdx+1

        if array[middleIdx] > array[leftIdx] and array[middleIdx] > array[rightIdx]:
            peakFound = True
        
        if peakFound:
            currentPeakLength = 3
            while leftIdx >= 1 and array[leftIdx-1] < array[leftIdx]:
                leftIdx -= 1
                currentPeakLength += 1
            while rightIdx < len(array)-1 and array[rightIdx+1] < array[rightIdx]:
                rightIdx += 1
                currentPeakLength += 1

            largestPeak = max(largestPeak, currentPeakLength)
            middleIdx = rightIdx
        else:
            middleIdx += 1

    return largestPeak
