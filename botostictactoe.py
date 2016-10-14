import random
import os

#Lena and Matyi TicTacToe

board = [" "] * 10
winvalues = ([7, 8, 9], [4, 5, 6], [1, 2, 3], [7, 4, 1,], [8, 5, 2], [9, 6, 3], [7, 5, 3], [9, 5, 1])
playermove = 0

#Draws the table
def table():
    print("\n")
    print(board[7], "|", board[8], "|", board[9])
    print("---------")
    print(board[4], "|", board[5], "|", board[6])
    print("---------")
    print(board[1], "|", board[2], "|", board[3])

#Checks if there is a full board
def boardfull():
    if " " in board[1:10]:
        print(" ")
    else:
        print("\nIt's a tie!")
        return "tie"

#Checks if there is a winner
def wincheck():
    for value in winvalues:
        if (board[(value[0])] == board[(value[1])] == board[(value[2])] == "x"):
            print("\nPlayer X won!\n")
            return "winner"           
        if (board[(value[0])] == board[(value[1])] == board[(value[2])] == "o"):
            print("\nPlayer 0 won!\n")
            return "winner"

#What robot is looking for
def robotpanic(x,y,z):
    if (board[x] == "o" and board[y] == "o" and board[z] == " " 
        or board[x] == "x" and board[y] == "x"  and board[z] == " "):
            board[z] = "o"
            return "block"

#Robot actions
def robotmove():
    while True:
        if robotpanic(7,8,9) == "block":
            break
        if robotpanic(4,5,6) == "block":
            break
        if robotpanic(1,2,3) == "block":
            break
        if robotpanic(7,4,1) == "block":
            break
        if robotpanic(8,5,2) == "block":
            break
        if robotpanic(9,6,3) == "block":
            break
        if robotpanic(7,5,3) == "block":
            break
        if robotpanic(9,5,1) == "block":
            break
        if robotpanic(7,9,8) == "block":
            break
        if robotpanic(4,6,5) == "block":
            break
        if robotpanic(1,3,2) == "block":
            break
        if robotpanic(7,1,4) == "block":
            break    
        if robotpanic(8,2,5) == "block":
            break
        if robotpanic(9,3,6) == "block":
            break
        if robotpanic(7,3,5) == "block":
            break
        if robotpanic(9,1,5) == "block":
            break
        if robotpanic(8,9,7) == "block":
            break
        if robotpanic(5,6,4) == "block":
            break
        if robotpanic(2,3,1) == "block":
            break
        if robotpanic(4,1,7) == "block":
            break
        if robotpanic(5,2,8) == "block":
            break
        if robotpanic(6,3,9) == "block":
            break
        if robotpanic(5,3,7) == "block":
            break
        if robotpanic(5,1,9) == "block":
            break         
        else:
            rn = random.randint(1, 9)
            if board[rn] != "o" and board[rn] != "x":
                board[rn] = "o"
                print("random")
                break


while True:
#The game
    print("Welcome to Lena and Matyi's TicTacToe Game!")
    print("\nChoose places with number keys:\n")
    print("7 | 8 | 9 \n4 | 5 | 6 \n1 | 2 | 3")
    start = input("\nWould you like to start the game? (y/n) ")
    if start == "y":
        robot = input("\nHow many players? (1/2): ")
        if robot == "1":
            break
        if robot == "2":
            plm = input("\nPlayer 1 choose X or O: ")
            if plm == "X" or plm == "x":
                playermove = 0
                break
            if plm == "O" or plm == "o":
                playermove = 1
                break
            
        else:
            continue
    if start == "n":
        print("Too bad :(")
        quit()
    else:
        continue

os.system('cls' if os.name == 'nt' else 'clear')
table()

while True:       
#First player
    while playermove == 0:
        n = input("\nPlayer X Choose a place: ")
        if not n.isdigit() or int(n) > 9:
            print("Please type a valid number! (1-9)")
            continue
        else:   
            n = int(n) 
            if board[n] != "x" and board[n] != "o":
                board[n] = "x"
                playermove += 1
            else:
                print(table)
                print("\nPlace already taken! Choose another one!")
    
    os.system('cls' if os.name == 'nt' else 'clear')
    table()
    if wincheck() == "winner" or boardfull() == "tie":
        restart = input("\nPlay again? (y/n) ")
        if restart == "y":
            os.system('cls' if os.name == 'nt' else 'clear')
            board = [" "] * 10
            table() 
        if restart == "n":
            quit()
    boardfull()
#Second player
    if robot == "2":    
        while playermove == 1:
            m = input("\nPlayer O Choose a place: ")
            if not m.isdigit() or int(m) > 9:
                print("Please type a valid number! (1-9) ")
                continue
            else:
                m = int(m)
                if board[m] != "x" and board[m] != "o":
                    board[m] = "o"
                    playermove -= 1
                else:
                    print("\nPlace already taken! Choose another one! ")
#Robot    
    while playermove == 1:  
        if robot == "1":
            robotmove()                                                          
            playermove -= 1
            
    os.system('cls' if os.name == 'nt' else 'clear')
    table() 
    if wincheck() == "winner" or boardfull() == "tie":
        restart = input("\nPlay again? (y/n) ")
        if restart == "y":
            os.system('cls' if os.name == 'nt' else 'clear')
            board = [" "] * 10
            table() 
        if restart == "n":
            quit()
    boardfull()

