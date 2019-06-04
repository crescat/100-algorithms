# Day 23: Sudoku

def solve(board):
    if not is_valid(board):
        raise Exception('sudoku board should be in size 9x9!')
    if is_finished(board):
        return board

    r, c = next_zero(board)
    possible_nums = find_possible_numbers(board, r, c)
    if len(possible_nums) == 0:
        return False

    candidate_boards = [put_number(board, r, c, num) for num in possible_nums]

    for candidate in candidate_boards:
        result = solve(candidate)
        if result:
            return result
    return False


def put_number(board, row, col, num):
    new_row = board[row][:col] + [num] + board[row][col+1:]
    return board[:row] + [new_row] + board[row+1:]


def next_zero(board):
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == 0:
                return (r, c)


def find_possible_numbers(board, row, col):
    valid_nums = set(range(1, 10))

    possible_nums =  valid_nums - set(board[row]) \
                                - set(transpose(board)[col]) \
                                - block(board, row, col)

    return (possible_nums | {board[row][col]}) - {0}


def is_valid(board):
    if len(board) != 9:
        return False
    for row in board:
        if len(row) != 9:
            return False
    return True


def is_finished(board):
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == 0:
                return False

    valid_nums = set(range(1, 10))

    for i in range(len(board)):
        if set(board[i]) != valid_nums:
            return False

    transposed_board = transpose(board)
    for i in range(len(board[0])):
        if set(transposed_board[i]) != valid_nums:
            return False

    for r, c in [(i*3, j*3) for i in range(3) for j in range(3)]:
        if block(board, r, c) != valid_nums:
            return False

    return True


def block(board, row, col):
    r, c = row//3*3, col//3*3
    return set(board[i][j] for i in range(r, r+3) for j in range(c, c+3))


def transpose(mtx):
    return [list(x) for x in zip(*mtx)]


def print_board(board):
    for row in board:
        print(row)


board = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

print_board(solve(board))
