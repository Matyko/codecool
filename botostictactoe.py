import random
import os

#Lena and Matyi TicTacToe

board = [" "] * 10
winvalues = ([7, 8, 9], [4, 5, 6], [1, 2, 3], [7, 4, 1,], [8, 5, 2], [9, 6, 3], [7, 5, 3], [9, 5, 1])
playermove = 0

def table():
    print("\n")
    print(board[7], "|", board[8], "|", board[9])
    print("---------")
    print(board[4], "|", board[5], "|", board[6])
    print("---------")
    print(board[1], "|", board[2], "|", board[3])

def boardfull():
    if " " in board[1:10]:
        print(" ")
    else:
        print("\nIt's a tie!")
        return "tie"

def wincheck():
    for value in winvalues:
        if (board[(value[0])] == board[(value[1])] == board[(value[2])] == "x"):
            print("\nPlayer X won!\n")
            return "winner"           
        if (board[(value[0])] == board[(value[1])] == board[(value[2])] == "o"):
            print("\nPlayer 0 won!\n")
            return "winner"

def robotmove():
    while True:
        if (board[7] == "x" and board[8] == "x" and board[9] == " " 
        or board[7] == "o" and board[8] == "o"  and board[9] == " "):
            board[9] = "o"
            break
        if (board[4] == "x" and board[5] == "x" and board[6] == " " 
        or board[4] == "o" and board[5] == "o" and board[6] == " "):
            board[6] = "o"
            break
        if (board[1] == "x" and board[2] == "x" and board[3] == " " 
        or board[1] == "o" and board[2] == "o" and board[3] == " "):
            board[3] = "o"
            break
        if (board[7] == "x" and board[4] == "x" and board[1] == " " 
        or board[7] == "o" and board[4] == "o" and board[1] == " "):
            board[1] = "o"
            break
        if (board[8] == "x" and board[5] == "x" and board[2] == " " 
        or board[8] == "o" and board[5] == "o" and board[2] == " "):
            board[2] = "o"
            break
        if (board[9] == "x" and board[6] == "x" and board[3] == " " 
        or board[9] == "o" and board[6] == "o" and board[3] == " "):
            board[3] = "o"
            break
        if (board[7] == "x" and board[5] == "x" and board[3] == " " 
        or board[7] == "o" and board[5] == "o" and board[3] == " "):
            board[3] = "o"
            break
        if (board[9] == "x" and board[5] == "x" and board[1] == " " 
        or board[9] == "o" and board[5] == "o" and board[1] == " "):
            board[1] = "o"
            break  
        if (board[7] == "x" and board[9] == "x" and board[8] == " " 
        or board[7] == "o" and board[9] == "o" and board[8] == " "):
            board[8] = "o"
            break
        if (board[4] == "x" and board[6] == "x" and board[5] == " " 
        or board[4] == "o" and board[6] == "o" and board[5] == " "):
            board[5] = "o"
            break
        if (board[1] == "x" and board[3] == "x" and board[2] == " " 
        or board[1] == "o" and board[3] == "o" and board[2] == " "):
            board[2] = "o"
            break
        if (board[7] == "x" and board[1] == "x" and board[4] == " " 
        or board[7] == "o" and board[1] == "o" and board[4] == " "):
            board[4] = "o"
            break
        if (board[8] == "x" and board[2] == "x" and board[5] == " " 
        or board[8] == "o" and board[2] == "o" and board[5] == " "):
            board[5] = "o"
            break
        if (board[9] == "x" and board[3] == "x" and board[6] == " " 
        or board[9] == "o" and board[3] == "o" and board[6] == " "):
            board[6] = "o"
            break
        if (board[7] == "x" and board[3] == "x" and board[5] == " " 
        or board[7] == "o" and board[3] == "o" and board[5] == " "):
            board[5] = "o"
            break
        if (board[9] == "x" and board[1] == "x" and board[5] == " " 
        or board[9] == "o" and board[1] == "o" and board[5] == " "):
            board[5] = "o"
            break  
        if (board[8] == "x" and board[9] == "x" and board[7] == " " 
        or board[8] == "o" and board[9] == "o" and board[7] == " "):
            board[7] = "o"
            break
        if (board[5] == "x" and board[6] == "x" and board[4] == " " 
        or board[5] == "o" and board[6] == "o" and board[4] == " "):
            board[4] = "o"
            break
        if (board[2] == "x" and board[3] == "x" and board[1] == " " 
        or board[2] == "o" and board[3] == "o" and board[1] == " "):
            board[1] = "o"
            break
        if (board[4] == "x" and board[1] == "x" and board[7] == " " 
        or board[4] == "o" and board[1] == "o" and board[7] == " "):
            board[7] = "o"
            break
        if (board[5] == "x" and board[2] == "x" and board[8] == " " 
        or board[5] == "o" and board[2] == "o" and board[8] == " "):
            board[8] = "o"
            break
        if (board[6] == "x" and board[3] == "x" and board[9] == " " 
        or board[6] == "o" and board[3] == "o" and board[9] == " "):
            board[9] = "o"
            break
        if (board[5] == "x" and board[3] == "x" and board[7] == " " 
        or board[5] == "o" and board[3] == "o" and board[7] == " "):
            board[7] = "o"
            break
        if (board[5] == "x" and board[1] == "x" and board[9] == " " 
        or board[5] == "o" and board[1] == "o" and board[9] == " "):
            board[9] = "o"
            break         
        else:
            rn = random.randint(1, 9)
            if board[rn] != "o" and board[rn] != "x":
                board[rn] = "o"
                print("random")
                break


while True:
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

