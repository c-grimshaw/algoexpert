def levenshteinDistance(str1: str, str2: str) -> int:
    """Returns the Levenshtein distance for a given number.
    
    The Levenshtein distance is equivalent to the number of edits
    (insert, delete, or substitute) required to transform s1 into s2.
    """

    table = [[0 for _ in range(0, len(str1)+1)] for _ in range(0, len(str2)+1)]
    
    # Seed top row
    for i in range(1, len(str1)+1):
        table[0][i] = i
    
    # Seed first column
    for i in range(1, len(str2)+1):
        table[i][0] = i

    for i in range(1, len(str2)+1):
        for j in range(1, len(str1)+1):
            table[i][j] = 1 + min(
                table[i-1][j-1],
                table[i-1][j],
                table[i][j-1]
            )
    
    return table[-1][-1]

print(levenshteinDistance('abc', 'yabd'))