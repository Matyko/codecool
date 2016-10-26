import random
import os

# Lena and Matyi TicTacToe

board = [" "] * 10
playermove = 0
robot = 0
playersymbol = 0
symbol = ["\033[95mX\033[00m", "\033[93mO\033[00m"]

winvalues = (
[7, 8, 9], [4, 5, 6], [1, 2, 3], [7, 4, 1], [8, 5, 2], [9, 6, 3], 
[7, 5, 3], [9, 5, 1], [9, 8, 7], [6, 5, 4], [3, 2, 1], [1, 4, 7], 
[2, 5, 8], [3, 6, 9], [3, 5, 7], [1, 5, 9], [1, 7, 4], [2, 8, 5], 
[3, 9, 6], [7, 9, 8], [4, 6, 5], [1, 3, 2], [7, 3, 5], [9, 1, 5])

# Draws the table

def table():
    print("\n")
    print(board[7], "|", board[8], "|", board[9])
    print("-"*9)
    print(board[4], "|", board[5], "|", board[6])
    print("-"*9)
    print(board[1], "|", board[2], "|", board[3])

#Lets player pick a symbolol

def symb():
    global symbol
    if playersymbol == "x" or playersymbol == "X":
        return
    if playersymbol == "o" or playersymbol == "O":
        symbol = ["\033[93mO\033[00m", "\033[95mX\033[00m"]
        return symbol

# Checks if there is a full board

def boardfull():
    if " " in board[1:10]:
        print(" ")
    else:
        print("\nIt's a tie!")
        return "tie"

# Checks if there is a winner

def wincheck():
    for value in winvalues:
        if (board[(value[0])] == board[(value[1])]
                == board[(value[2])] == symbol[0]):
            print("\033[92m\nPlayer X won!\n\033[00m")
            return "winner"
        if (board[(value[0])] == board[(value[1])]
                == board[(value[2])] == symbol[1]):
            print("\033[92m\nPlayer O won!\n\033[00m")
            return "winner"

def clean():
    os.system('cls' if os.name == 'nt' else 'clear')
    return

# What robot is looking for

def robotnotforwin(x, y):
    if board[x] == symbol[1] and board[y] == " ":
        board[y] = symbol[1]
        print("többször")
        return "rmove"

def robotpanic(x, y, z):
    if (board[x] == symbol[0] and board[y] == symbol[0] and board[z] == " "):
        return "block"
    if (board[x] == symbol[1] and board[y] == symbol[1] and board[z] == " "):    
        return "block"

# Robot actions

def randompick():
    rn = random.randint(1, 9)
    if board[rn] != symbol[1] and board[rn] != symbol[0]:
        board[rn] = symbol[1]
        print("random")

    
def robotmove():
    for value in winvalues:
        if board[5] != symbol[0] and symbol[1] not in board:
            board[5] = symbol[1]
            return
        elif robotpanic(value[0], value[1], value[2]) == "block":
            if board[value[2]] !=symbol[0]:
                board[value[2]] = symbol[1]
                print("!!!", value[0], value[1], value[2])
                return
            else:
                randompick()
    randompick()

# Start and settings

def start():
    global playermove
    global robot
    global playersymbol
    print("Welcome to Lena and Matyi's TicTacToe Game!\n\nChoose places with number keys:\n\n7 | 8 | 9 \n4 | 5 | 6 \n1 | 2 | 3")
    while robot == 0:    
        start = input("\nWould you like to start the game? (Yes / No) ")
        while start == "Yes" or start == "yes":
            robot = input("\nHow many players? (1/2): ")
            while robot == "1" or robot == "2":    
                playersymbol = input("\nPlayer 1 choose X or O: ")
                if playersymbol == "x" or playersymbol == "o" or playersymbol == "X" or playersymbol == "O":
                    return
                else:
                    print("Choose a valid input!")
            else:
               print("Choose a valid input!") 
        
        if start == "No" or start == "no":
            print("Too bad :(")
            quit()
        else:
            print("Choose a valid input!")

start()
symb()
clean()
table()

while True:

    # First player

    while playermove == 0:
        n = input("\nPlayer " + symbol[0] + " Choose a place: ")
        if not n.isdigit() or int(n) > 9:
            print("Please type a valid number! (1-9)")
            continue
        else:
            n = int(n)
            if board[n] != symbol[0] and board[n] != symbol[1]:
                board[n] = symbol[0]
                playermove += 1
            else:
                print(table)
                print("\nPlace already taken! Choose another one!")

    clean()
    table()
    if wincheck() == "winner" or boardfull() == "tie":
        restart = input("\nPlay again? (Yes / No) ")
        if restart == "Yes" or restart == "yes":
            clean()
            board = [" "] * 10
            table()
        if restart == "No" or restart == "no":
            quit()
    boardfull()

# Second player

    if robot == "2":
        while playermove == 1:
            m = input("\nPlayer " + symbol[1] + " Choose a place: ")
            if not m.isdigit() or int(m) > 9:
                print("Please type a valid number! (1-9) ")
                continue
            else:
                m = int(m)
                if board[m] != symbol[0] and board[m] != symbol[1]:
                    board[m] = symbol[1]
                    playermove -= 1
                else:
                    print("\nPlace already taken! Choose another one! ")

# Robot

    while playermove == 1:
        if robot == "1":
            robotmove()
            playermove -= 1

    clean()
    table()
    if wincheck() == "winner" or boardfull() == "tie":
        restart = input("\nPlay again? (Yes / No) ")
        if restart == "Yes" or restart == "yes":
            clean()
            board = [" "] * 10
            table()
        if restart == "no" or restart == "No":
            quit()
    boardfull()
