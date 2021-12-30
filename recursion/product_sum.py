def productSum(array: list[int], depth: int = 1) -> int:
    """
    [x, [y, [z]]] == x + 2(y+3z)
    """
    if len(array) == 0:
        return 0
    if isinstance(array[0], int):
        return array[0] + productSum(array[1:], depth)
    else:
        return (depth + 1) * (productSum(array[0], depth + 1)) + productSum(array[1:])
