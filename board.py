def print_board(board):
    print(board[0])
    print(board[1])
    print(board[2])


def end_game_p1(board):
    is_won = False

    # check rows for three 1's
    rows = [0, 1, 2]
    for i in rows:
        if board[i][0] == '1' and board[i][1] == '1' and board[i][2] == '1':
            is_won = True
            print('Player 1 won!')
            break

    # If player did not win on rows, try columns
    if is_won == False:
        cols = [0, 1, 2]
        for i in cols:
            if board[0][i] == '1' and board[1][i] == '1' and board[2][i] == '1':
                is_won = True
                print('Player 1 won!')
                break

    # If columns did not win, try the diagonals
    if is_won == False:
        if board[0][0] == '1' and board[1][1] == '1' and board[2][2] == '1':
            is_won = True
            print('Player 1 won!')

    if is_won == False:
        if board[0][2] == '1' and board[1][1] == '1' and board[2][0] == '1':
            is_won = True
            print('Player 1 won!')

    return is_won


def end_game_p2(board):
    is_won = False

    # check rows for three 1's
    rows = [0, 1, 2]
    for i in rows:
        if board[i][0] == '2' and board[i][1] == '2' and board[i][2] == '2':
            is_won = True
            print('Player 2 won!')
            break

    # If player did not win on rows, try columns
    if is_won == False:
        cols = [0, 1, 2]
        for i in cols:
            if board[0][i] == '2' and board[1][i] == '2' and board[2][i] == '2':
                is_won = True
                print('Player 2 won!')
                break

    # If columns did not win, try the diagonals
    if is_won == False:
        if board[0][0] == '2' and board[1][1] == '2' and board[2][2] == '2':
            is_won = True
            print('Player 2 won!')

    if is_won == False:
        if board[0][2] == '2' and board[1][1] == '2' and board[2][0] == '2':
            is_won = True
            print('Player 2 won!')

    return is_won


# create board
list1 = ['-', '-', '-']
list2 = ['-', '-', '-']
list3 = ['-', '-', '-']
board = [list1, list2, list3]

print_board(board)

isPlaying = True
while isPlaying:

    # player one input
    isValid = False
    while not isValid:

        row = input("Player One, Enter Row (1-3):")
        while row != "1" and row != "2" and row != "3":
            print("Invalid Entry\n")
            row = input("Player One, Enter Row (1-3):")
        row = int(row)
        row -= 1

        column = input("Player One, Enter Column (1-3):")
        while column != "1" and column != "2" and column != "3":
            print("Invalid Entry\n")
            column = input("Player One, Enter Column (1-3):")
        column = int(column)
        column -= 1

        if board[row][column] == "-":
            isValid = True
        else:
            print("Space Already Taken\n")

    board[row][column] = "1"

    print_board(board)

    # See if p1 won
    game_over = end_game_p1(board)

    # Check for a draw
    if not game_over:
        board_full = True
        for i in board:
            if '-' in i:
                board_full = False
        if board_full:
            print('Draw')
            game_over = True

    if game_over:
        break

    # player 2 input
    isValid = False
    while not isValid:
        row = input("Player Two, Enter Row (1-3):")
        while row != "1" and row != "2" and row != "3":
            print("Invalid Entry\n")
            row = input("Player Two, Enter Row (1-3):")
        row = int(row)
        row -= 1

        column = input("Player Two, Enter Column (1-3):")
        while column != "1" and column != "2" and column != "3":
            print("Invalid Entry\n")
            column = input("Player Two, Enter Column (1-3):")
        row = int(row)
        column = int(column)
        column -= 1

        if board[row][column] == "-":
            isValid = True
        else:
            print("Space Already Taken\n")

    board[row][column] = "2"
    print_board(board)

    # See if p2 won
    game_over = end_game_p1(board)

    # Check for a draw
    if not game_over:
        board_full = True
        for i in board:
            if '-' in i:
                board_full = False
        if board_full:
            print('Draw')
            game_over = True

    if game_over:
        break


