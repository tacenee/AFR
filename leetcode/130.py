def solve(board) -> None:
    if not board: return
    row = len(board)
    col = len(board[0])
    if row < 3 or col < 3: return

    def dfs(x, y):
        if x < 0 or x >= row or y < 0 or y >= col or board[x][y] != 'O':
            return
        board[x][y] = '#'
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)

    for i in range(row):
        dfs(i, 0)
        dfs(i, col - 1)

    for j in range(col):
        dfs(0, j)
        dfs(row - 1, j)

    for r in range(row):
        for c in range(col):
            if board[r][c] == 'O':
                board[r][c] = 'X'
            if board[r][c] == '#':
                board[r][c] = 'O'
    return


nums = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]

solve(nums)
print(nums)
