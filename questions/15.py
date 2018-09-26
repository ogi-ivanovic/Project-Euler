board = [[1]*21]
row = [1] + [0]*20
rows = [row]*20
board = board + rows

for row in range(1, 21):
  for column in range(1, 21):
    board[row][column] = board[row - 1][column] + board[row][column - 1]

print(board[20][20])
