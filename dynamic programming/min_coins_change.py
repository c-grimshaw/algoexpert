def minNumberOfCoinsForChange(n: int, denoms: list[int]) -> int:
    """
    Returns the minimum number of coins required to produce the target n, given a list of denominations.

    e.g., n = 7, denoms = [1, 5, 10] --> 3 (2 x 1, 5 x 1)
    """

    coins = [float('inf') for amount in range(n+1)]
    coins[0] = 0

    for denom in denoms:
        for amount in range(0, len(coins)):
            if denom <= amount: 
                coins[amount] = min(coins[amount], coins[amount-denom]+1)

    return coins[n] if coins[n] != float('inf') else -1