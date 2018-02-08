import random
import os
import highscore
import datetime


def createEmptyBoard():
    board = []
    sample = True
    while sample:
        checker = makeBoard()
        if checker is not True:
            sample = False
            board = checker
    return board


def makeBoard():

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
    os.system("clear")
    print("\033[94m\033[1m    1 2 3   4 5 6   7 8 9 ")
    print("\033[93m\033[1m  ┌───────┬───────┬───────┐")
    for i in range(9):
        for j in range(9):
            if j == 0:
                if (i, j) not in empty:
                    print("\033[94m\033[1m" + str(i + 1) + "\033[93m\033[1m │ \033[91m\033[1m" + str(board[i][j]), end=" ")
                else:
                    print("\033[94m\033[1m" + str(i + 1) + "\033[93m\033[1m │ \033[92m\033[1m" + str(board[i][j]), end=" ")
            elif j == 2 or j == 5 or j == 8:
                if (i, j) not in empty:
                    print("\033[91m\033[1m" + str(board[i][j]), end="\033[93m\033[1m │ ")
                else:
                    print("\033[92m\033[1m" + str(board[i][j]), end="\033[93m\033[1m │ ")
            else:
                if (i, j) not in empty:
                    print("\033[91m\033[1m" + str(board[i][j]), end=" ")
                else:
                    print("\033[92m\033[1m" + str(board[i][j]), end=" ")
        if i == 2 or i == 5:
            print("\033[93m\033[1m\n  ├───────┼───────┼───────┤")
        else:
            print()
    print("\033[93m\033[1m  └───────┴───────┴───────┘")
    return None


# Checks  for rows, cols and 3x3 blocks
def checkRandom(sample):
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
    empty = []
    counter = 0
    while counter < difficulty:
        x = random.randint(0, 8)
        y = random.randint(0, 8)
        if board[x][y] != "∙":
            board[x][y] = "∙"
            empty.append(tuple([x, y]))
            counter += 1
    print(sorted(empty))
    return board, empty


# Input
def enter_nums(empty, board):

    # We save the numbers in a list
    try:
        num = [int(x) for x in input("\033[92m\033[1mEnter the numbers: ").strip(" ").split(" ")]
        print()

        # The delete function
        if len(num) == 2:
            if num[0] < 10 and num[0] > 0 and num[1] < 10 and num[1] > 0:
                num[0] -= 1
                num[1] -= 1
                board = delete_number(empty, board, num)
            else:
                print("\033[91m\033[1mWrong input!")
                return enter_nums(empty, board)
        elif len(num) == 3:
            if num[0] < 10 and num[0] > 0 and num[1] < 10 and num[1] > 0 and num[2] < 10 and num[2] > 0:
                num[0] -= 1
                num[1] -= 1
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
    sample = tuple(sample)
    if sample in empty:
        board[sample[1]][sample[0]] = "∙"
    else:
        os.system("clear")
        printBoard(empty, board)
        print("\033[91m\033[1mThat is an original number!")
        enter_nums(empty, board)
    return board


def write(empty, board, sample):
    sample_coord = (sample[1], sample[0])
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
    for i in range(9):
        for j in range(9):
            if sample[i][j] == "∙":
                return False
            else:
                continue
    return True


def startTimer():
    return datetime.datetime.now()


def endTimer(currentTime, difficulty):
    ending = datetime.datetime.now()
    final = (ending-currentTime).total_seconds()
    if difficulty == 10:
        score = round(300 - final)
    elif difficulty == 55:
        score = round(600 - final)
    elif difficulty == 65:
        score = round(1200 - final)
    if score < 0:
        score = 0
    print(score)
    return score


def startGame():
    while True:
        try:
            os.system("clear")
            print("\033[94m\033[1mSUDOKU\n\nTo write into the board, enter 3 numbers: row(1-9), column(1-9), number(1-9).")
            print("To delete from the board, enter 2 numbers: row(1-9), column(1-9).")
            print("Choose a difficulty:")
            print("   Easy - 1")
            print("   Medium - 2")
            print("   Hard - 3")
            text = input().strip()
            if text == "1":
                return 10
            elif text == "2":
                return 55
            elif text == "3":
                return 65
        except TypeError:
            continue


def main():
    diff = startGame()
    startTime = startTimer()
    example = createEmptyBoard()
    example, empty_list = deleteRandom(example, diff)
    printBoard(empty_list, example)
    while True:
        if checkEmpty(example):
            if checkRandom(example):
                highscore.highScoreProcess(endTimer(startTime, diff))
                break
        example = enter_nums(empty_list, example)
        printBoard(empty_list, example)


if __name__ == "__main__":
    main()
