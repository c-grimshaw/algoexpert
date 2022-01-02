def numberOfWaysToTraverseGraph(width: int, height: int, memo={}) -> int:
    """
    Returns the number of ways to traverse a grid-like structure, assuming you can only
    move down or right.

    ._._.
    |_._|
    |_._|
    |_._| --> 3
    """
    if width == 1 or height == 1:
        return 1

    memo[f"{width}+{height}"] = numberOfWaysToTraverseGraph(
        width - 1, height, memo
    ) + numberOfWaysToTraverseGraph(width, height - 1, memo)
    return memo[f"{width}+{height}"]
