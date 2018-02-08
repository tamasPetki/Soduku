import csv


def highScoreProcess(score):
    highscorelist = openHighscore()
    if checkHighscore(score, highscorelist) or len(highscorelist) == 0:
        name = highScore()
        modified_scorelist = addNewScore(score, name, highscorelist)
        printHighscore(modified_scorelist)
        writeHighscore(modified_scorelist)
        return
    printHighscore(highscorelist)
    input()
    return


def highScore():
    name = input("You are in the TOP 10! What's your name? : ")
    return name


def addNewScore(score, name, scorelist):
    if len(scorelist) == 0:
        new_element = [name, score]
        scorelist.append(new_element)
        return scorelist
    for i in range(len(scorelist)):
        if score >= scorelist[i][1]:
            scorelist.insert(i, [name, score])
            break
    if len(scorelist) > 10:
        del scorelist[10]
    return scorelist


def openHighscore():
    try:
        with open('highscoretable.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            readedList = []
            for row in readCSV:
                name_score = [row[0],int(row[1])]
                readedList.append(name_score)
    except FileNotFoundError:
        readedList = []
    return readedList


def writeHighscore(newScore):
    highfile = open('highscoretable.csv', 'w')  
    writer = csv.writer(highfile)
    writer.writerows(newScore)
    highfile.close()


def printHighscore(readedList):
    print("\nTOP 10 - HIGH SCORE")
    print("-------------------\n")
    for i in range(len(readedList)):
        print(str(readedList[i][0]).ljust(11), str(readedList[i][1]).rjust(7))


def checkHighscore(score, highlist):
    for i in highlist:
        if score >= i[1]:
            return True
    return False
