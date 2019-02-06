from random import*


def createboard(level, option):
    if option.lower() == "easy":
        level = 7
    elif option.lower() == "medium":
        level = 9
    elif option.lower() == "hard":
        level = 12
    for i in range(0, level):
        board.append([])
        for j in range(0, level):
            board[i].append(" ")
    return level


def word(lines, choose):
    while choose < level:
        randomnum = randint(0, 99)
        wordC = lines[randomnum]
        if word not in chosen:
            chosen.append(wordC.strip())
            choose = choose + 1


def addwords():
    direction = randint(1, 2)
    for i in range(0, level):
        walk = 1
        while walk == 1:
            if len(chosen[i]) == 3:
                xlocation = randint(0, level-3)
                ylocation = randint(0, level-1)
                if board[ylocation][xlocation] == " " and board[ylocation][xlocation+1] == " " and board[ylocation][xlocation+2] == " ":
                    splitword = list(chosen[i])
                    if direction == 1:
                        for j in range(0, len(splitword)):
                            board[ylocation][xlocation+j] = (splitword[j])
                    else:
                        for j in range(0, len(splitword)):
                            board[ylocation][xlocation+3-j] = (splitword[j])
                    walk = 2
            elif len(chosen[i]) == 4:
                print("4")
                walk = 2
            elif len(chosen[i]) == 5:
                print("5")
                walk = 2
            elif len(chosen[i]) == 6:
                print("6")
                walk = 2

'''
def add():
    length =
    for i in range (0, length):
'''


pick = 1
level = 0
randomnum = 0
choose = 0
board = []
chosen = []
splitword = []
lines = open("words.txt", "r").readlines()

option = input("Choose level: Easy, Medium, Hard.\n")
while option.lower() != "easy" and option.lower() != "medium" and option.lower() != "hard":
    option = input("Choose level: Easy, Medium, Hard.\n")
level = createboard(level, option)
(word(lines, choose))
addwords()
print(chosen)

for i in range(level):
    print(board[i])
