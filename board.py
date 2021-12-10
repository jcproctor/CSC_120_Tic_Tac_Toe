def print_board(board):
    print(board[0])
    print(board[1])
    print(board[2])


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


