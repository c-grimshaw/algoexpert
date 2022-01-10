def removeIslands(matrix):
    visited = set()
    
    # Traverse top border
    for col in range(0, len(matrix[0])):
        dfs(0, col, matrix, visited)
    
    # Traverse right border
    for row in range(0, len(matrix)):
        dfs(row, len(matrix[0])-1, matrix, visited)

    # Traverse bottom border
    for col in range(0, len(matrix[0])):
        dfs(len(matrix)-1, col, matrix, visited)
    
    # Traverse left border
    for row in range(0, len(matrix)):
        dfs(row, 0, matrix, visited)
    
    # Finally, remove non-visited ones.
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[0])):
            if matrix[row][col] == 1 and (row, col) not in visited:
                matrix[row][col] = 0

    return matrix


def getNeighbours(row, col, matrix, visited):
    neighbours = []
    # Check above
    if (
        row > 0 and
        matrix[row-1][col] == 1 and
        (row-1, col) not in visited
        ): neighbours.append((row-1, col))

    # Check below
    if (
        row < len(matrix) - 1 and
     matrix[row+1][col] == 1 and
     (row+1, col) not in visited
    ): neighbours.append((row+1, col))

    # Check left
    if (
        col > 0 and
         matrix[row][col-1] == 1 and
         (row, col-1) not in visited
    ): neighbours.append((row, col-1))

    # Check right
    if (
        col < len(matrix[0]) - 1 and
        matrix[row][col+1] == 1 and
        (row, col+1) not in visited
    ): neighbours.append((row, col+1))
    return neighbours

def dfs(row, col, matrix, visited):
    if matrix[row][col] == 0:
        return
    neighbours = getNeighbours(row, col, matrix, visited)
    visited.add((row, col))
    for neighbour in neighbours:
        row, col = neighbour
        dfs(row, col, matrix, visited)


matrix = [
  [1, 0, 0, 0, 0, 0],
  [0, 1, 0, 1, 1, 1],
  [0, 0, 1, 0, 1, 0],
  [1, 1, 0, 0, 1, 0],
  [1, 0, 1, 1, 0, 0],
  [1, 0, 0, 0, 0, 1],
]

result = [
  [1, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 1, 1],
  [0, 0, 0, 0, 1, 0],
  [1, 1, 0, 0, 1, 0],
  [1, 0, 0, 0, 0, 0],
  [1, 0, 0, 0, 0, 1],
] 

assert removeIslands(matrix) == result