import random
import os
import highscore
import datetime


def createEmptyBoard():
    """ Will call makeBoard constantly until a good table is not given """
    board = []
    sample = True

    # Will pass this only if the table is complete and correct
    while sample:
        checker = makeBoard()
        if checker is not True:
            sample = False
            board = checker
    
    # Returns the complete random generated board
    return board


def makeBoard():
    """ Tries to create an empty board, if it can no be completed, throws it out """

    # Making the empty board
    board = []
    for i in range(9):
        board.append([])
        for j in range(9):
            board[i].append("∙")

    # Filling the board
    for i in range(9):
        for j in range(9):
            current = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            random.shuffle(current)

            # Indexig number
            list_index = -1

            # Checking current number
            while board[i][j] == "∙":
                list_index += 1

                # If none of the numbers are good
                if list_index == 9:
                    # makeBoard()
                    return True

                # Checking current row
                if current[list_index] in board[i]:
                    continue

                # Checking current column
                checkCol = False
                for column in board:
                    if column[j] == current[list_index]:
                        checkCol = True
                if checkCol:
                    continue
                
                # Checking 3x3 blocks
                if i % 3 == 1:
                    if j % 3 == 0:
                        if board[i-1][j+1] == current[list_index] or board[i-1][j+2] == current[list_index] or board[i+1][j+1] == current[list_index] or board[i+1][j+2] == current[list_index]:
                            continue
                    elif j % 3 == 1:
                        if board[i-1][j-1] == current[list_index] or board[i+1][j-1] == current[list_index] or board[i-1][j+1] == current[list_index] or board[i+1][j+1] == current[list_index]:
                            continue
                    elif j % 3 == 2:
                        if board[i-1][j-2] == current[list_index] or board[i-1][j-1] == current[list_index] or board[i+1][j-2] == current[list_index] or board[i+1][j-1] == current[list_index]:
                            continue
                elif i % 3 == 2:
                    if j % 3 == 0:
                        if board[i-2][j+1] == current[list_index] or board[i-2][j+2] == current[list_index] or board[i-1][j+1] == current[list_index] or board[i-1][j+2] == current[list_index]:
                            continue
                    elif j % 3 == 1:
                        if board[i-2][j-1] == current[list_index] or board[i-1][j-1] == current[list_index] or board[i-2][j+1] == current[list_index] or board[i-1][j+1] == current[list_index]:
                            continue
                    elif j % 3 == 2:
                        if board[i-2][j-2] == current[list_index] or board[i-2][j-1] == current[list_index] or board[i-1][j-2] == current[list_index] or board[i-1][j-1] == current[list_index]:
                            continue

                board[i][j] = current[list_index]
    return board


def printBoard(empty, board):
    """ Prints the whole board out """
    os.system("clear")

    # Starting frame
    print("\033[94m\033[1m    1 2 3   4 5 6   7 8 9 ")
    print("\033[93m\033[1m  ┌───────┬───────┬───────┐")

    # Printing table elements
    for i in range(9):
        for j in range(9):

            # First column starts with number and frame part
            if j == 0:

                # Deciding if the number is original or not
                if (i, j) not in empty:
                    print("\033[94m\033[1m" + str(i + 1) + "\033[93m\033[1m │ \033[91m\033[1m" + str(board[i][j]), end=" ")
                else:
                    print("\033[94m\033[1m" + str(i + 1) + "\033[93m\033[1m │ \033[92m\033[1m" + str(board[i][j]), end=" ")

            # Middle frame parts
            elif j == 2 or j == 5 or j == 8:

                # Deciding if the number is original or not
                if (i, j) not in empty:
                    print("\033[91m\033[1m" + str(board[i][j]), end="\033[93m\033[1m │ ")
                else:
                    print("\033[92m\033[1m" + str(board[i][j]), end="\033[93m\033[1m │ ")
            else:

                # Deciding if the number is original or not
                if (i, j) not in empty:
                    print("\033[91m\033[1m" + str(board[i][j]), end=" ")
                else:
                    print("\033[92m\033[1m" + str(board[i][j]), end=" ")

        # Printing lines between 3x3 blocks
        if i == 2 or i == 5:
            print("\033[93m\033[1m\n  ├───────┼───────┼───────┤")
        else:
            print()
    
    # Ending frame
    print("\033[93m\033[1m  └───────┴───────┴───────┘")
    return None


# Checks  for rows, cols and 3x3 blocks
def checkRandom(sample):
    """ Checks if the solution is good or not """
    total = 45
    sum = 0

    # Checks rows
    for i in range(9):
        for j in range(9):
            sum = sum + int(sample[i][j])
        if total != sum:
            print("\033[91m\033[1mWrong solution!")
            return False
        else:
            sum = 0

    # Checks columns
    for i in range(9):
        for j in range(9):
            sum = sum + int(sample[j][i])
        if total != sum:
            print("\033[91m\033[1mWrong solution!")
            return False
        else:
            sum = 0

    # Checks 3x3 blocks
    for n in range(0, 9, 3):
        for m in range(0, 9, 3):
            for i in range(0 + n, 3 + n):
                for j in range(0 + m, 3 + m):
                    sum = sum + int(sample[i][j])
            if total != sum:
                print("\033[91m\033[1mWrong solution!")
                return False
            else:
                sum = 0

    # If rows, cols and blocks are checked, we are good
    print("\033[92m\033[1mGood solution!")
    print()
    return True


def deleteRandom(board, difficulty=45):
    """ Deletes elements based on difficulty from the gives filled out board """
    empty = []
    counter = 0

    # Picking random numbers
    while counter < difficulty:
        x = random.randint(0, 8)
        y = random.randint(0, 8)

        # Removing numbers
        if board[x][y] != "∙":
            board[x][y] = "∙"

            # Making 2D tuple of numbers deleted here (by coordinates) for later use
            empty.append(tuple([x, y]))
            counter += 1

    # Returns the partially deleted board, and the tuple with the coordinates
    return board, empty


# Input
def enter_nums(empty, board):
    """ Handles the number input """

    # We save the numbers in a list
    try:
        num = [int(x) for x in input("\033[92m\033[1mEnter the numbers: ").strip(" ").split(" ")]
        print()

        # If we want to delete from the board
        if len(num) == 2:
            # Checking if conditions for it are good
            if num[0] < 10 and num[0] > 0 and num[1] < 10 and num[1] > 0:
                num[0] -= 1
                num[1] -= 1
                # Calling delete function on the board
                board = delete_number(empty, board, num)
            else:
                print("\033[91m\033[1mWrong input!")
                return enter_nums(empty, board)
        # If we want to write to the board
        elif len(num) == 3:
            # Checking if conditions for it are good
            if num[0] < 10 and num[0] > 0 and num[1] < 10 and num[1] > 0 and num[2] < 10 and num[2] > 0:
                num[0] -= 1
                num[1] -= 1
                # Calling write function on the board
                board = write(empty, board, num)
            else:
                print("\033[91m\033[1mWrong input!")
                return enter_nums(empty, board)
        else:
            print("\033[91m\033[1mWrong input format!")
            return enter_nums(empty, board)
    except ValueError:
        print("\033[91m\033[1mInvalid input!")
        return enter_nums(empty, board)
    return board


def delete_number(empty, board, sample):
    """ Deleting the given number (by coodrinates->sample) from the given table(board)
    based on the deletable elements(empty) """
    sample_coord = (sample[1], sample[0])
    # Checking if it is not an originally given number
    if sample_coord in empty:
        board[sample[1]][sample[0]] = "∙"
    else:
        os.system("clear")
        printBoard(empty, board)
        print("\033[91m\033[1mThat is an original number!")
        enter_nums(empty, board)
    return board


def write(empty, board, sample):
    """ Writes to the given table(board) based on the coordinates (sample) given
    based on the writeable elements(empty) """
    sample_coord = (sample[1], sample[0])
    # Checking if it is not an originally given number
    if sample_coord in empty:
        board[sample[1]][sample[0]] = sample[2]
    else:
        os.system("clear")
        printBoard(empty, board)
        print("\033[91m\033[1mThat is an original number!")
        enter_nums(empty, board)
    return board


# Checking if the board if full
def checkEmpty(sample):
    """ Checking if there is anymore blank spaces we can write to """
    for i in range(9):
        for j in range(9):
            if sample[i][j] == "∙":
                return False
            else:
                continue
    return True


def startTimer():
    """ Saves the time for the Score for later """
    return datetime.datetime.now()


def endTimer(currentTime, difficulty):
    """ Calculates the time spent on the puzzle, calculating score """
    ending = datetime.datetime.now()
    # Total time spent in seconds
    final = (ending-currentTime).total_seconds()
    # Calculating score based on time and difficulty
    if difficulty == 10:
        score = round(300 - final)
    elif difficulty == 55:
        score = round(600 - final)
    elif difficulty == 65:
        score = round(1200 - final)
    if score < 0:
        score = 0
    return score


def startGame():
    """ Main menu, describtion, rules, difficulty choosing """
    while True:
        try:
            # Description, choosing difficulty
            os.system("clear")
            print("\033[94m\033[1mSUDOKU\n\nTo write into the board, enter 3 numbers: row(1-9), column(1-9), number(1-9).")
            print("To delete from the board, enter 2 numbers: row(1-9), column(1-9).")
            print("Choose a difficulty:")
            print("   Easy - 1")
            print("   Medium - 2")
            print("   Hard - 3")
            text = input().strip()
            # Handling difficulty
            if text == "1":
                return 10
            elif text == "2":
                return 55
            elif text == "3":
                return 65
        except TypeError:
            continue


def main():
    """ Main function, soul of the program """
    # Starting game, difficulty
    diff = startGame()
    # Saving time
    startTime = startTimer()
    # Creating and deleting from the table
    example = createEmptyBoard()
    example, empty_list = deleteRandom(example, diff)
    printBoard(empty_list, example)
    # Entering numbers, checking if solution is good or bad
    while True:
        if checkEmpty(example):
            if checkRandom(example):
                # Using highscore module to calculate highscore
                highscore.highScoreProcess(endTimer(startTime, diff))
                break
        example = enter_nums(empty_list, example)
        printBoard(empty_list, example)


if __name__ == "__main__":
    main()
