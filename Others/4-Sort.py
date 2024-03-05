def solution(Board):
    res = float('-inf')
    for i in range(len(Board)):
        for j in range(len(Board[0])):
            visited = [[False] * len(Board[0]) for _ in range(len(Board))]
            res = max(res, biggestNumber(Board, i, j, visited, ''))
    return res


def biggestNumber(Board, row, column, visited, current):
    if row < 0 or column < 0 or row >= len(Board) or column >= len(Board[0]) or visited[row][column]:
        return 0
    current += str(Board[row][column])
    if len(current) == 4:
        return int(current)

    stack = []
    neighbors = ((1, 0), (0, 1), (-1, 0), (0, -1))
    visited[row][column] = True
    for dr, dc in neighbors:
        stack.append(biggestNumber(Board, dr + row, dc + column, visited, current))

    return max(stack)


'''Board = [[9,1,1,0,7],
         [1,0,2,1,0],
         [1,9,1,1,0]]
print(solution(Board))'''



Board = [[0, 1, 5, 0, 0]]
print(solution(Board))