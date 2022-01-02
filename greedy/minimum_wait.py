def minimumWait(queries: list[int]) -> int:
    """Returns the minimum waiting time, given a sequence of queries
    
    A query's waiting time is defined as the total time it takes to execute
    all queries before the current.
    """
    queries.sort()

    totalWait = currentWait = 0
    for i in range(0, len(queries)-1):
        currentWait += queries[i]
        totalWait += currentWait

    return totalWait