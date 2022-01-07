def powerset(array: list[int]) -> list[list[int]]:
    subsets = []
    powersetHelper(array, [], subsets)
    return subsets

def powersetHelper(array, currentSet, sets):
    sets.append(currentSet)
    if len(array) == 0:
        return

    for i in range(0, len(array)):
        newArray = array[i+1:]
        newSet = currentSet + [array[i]]
        powersetHelper(newArray, newSet, sets)
