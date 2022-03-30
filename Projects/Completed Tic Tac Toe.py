from array import array
from ast import Call


curent_player = 1
GameProcess = "Still"
next_mark = None

WinCheck = 0

gameboard = [
  ".",".",".",
  ".",".",".",
  ".",".","."
  ]

def WinCheckTo():
    if  gameboard[0] == gameboard[4] and gameboard[4] == gameboard[8] and gameboard[0] != ".":
        GameProcess = "Stop"
        WinCheck = 1
        print(next_mark,"win")
        quit()
    elif gameboard[2] != "." and gameboard[2] == gameboard[4] and gameboard[4] == gameboard[6]:
        GameProcess = "Stop"
        WinCheck = 1 
        print(next_mark, "win")
        quit()
    elif gameboard[3] != "." and gameboard[3] == gameboard[4] and gameboard[4] == gameboard[5]:
        GameProcess = "Stop"
        WinCheck = 1
        print(next_mark, "win")
        quit()
    elif gameboard[0] != "." and gameboard[0] == gameboard[1] and gameboard[1] == gameboard[2]:
        GameProcess = "Stop"
        WinCheck = 1
        print(next_mark, "win")
        quit()
    elif gameboard[6] != "." and gameboard[6] == gameboard[7] and gameboard[7] == gameboard[8]:
        GameProcess = "Stop"
        WinCheck = 1
        print(next_mark, "win")
        quit()
    elif gameboard[0] != "." and gameboard[0] == gameboard[3] and gameboard[3] == gameboard[6]:
        GameProcess = "Stop"
        WinCheck = 1
        print(next_mark, "win")
        quit()
    elif gameboard[1] != "." and gameboard[1] == gameboard[4] and gameboard[4] == gameboard[7]:
        GameProcess = "Stop"
        WinCheck = 1
        print(next_mark, "win")
        quit()
    elif gameboard[2] != "." and gameboard[2] == gameboard[5] and gameboard[5] == gameboard[8]:
        GameProcess = "Stop"
        WinCheck = 1
        print(next_mark, "win")
        quit()
    elif gameboard[0] != "." and gameboard[1] != "." and gameboard[2] != "." and gameboard[3] != "." and gameboard[4] != "." and gameboard[5] != "." and gameboard[6] != "." and gameboard[7] != "." and gameboard[8] != ".": 
        GameProcess = "Stop"
        WinCheck = 1
        print("DRAW!")
        quit()
    else:
        GameProcess = "Still"

def FreeCheck(z):
    if gameboard[z] == ".":
        return True
    else:
        return False


def CallGame():
  print(gameboard[0], gameboard[1], gameboard[2])
  print(gameboard[3], gameboard[4], gameboard[5])
  print(gameboard[6], gameboard[7], gameboard[8])


while  WinCheck == 0 :
    CallGame()
    WinCheckTo()
    if(curent_player % 2 != 0):
        next_mark = "X"
    else:
        next_mark = "O"
    next_point = int(input("Input where you want place your mark: "))
    next_point -= 1
    if(FreeCheck(next_point)):
        gameboard[next_point] = next_mark
        curent_player += 1
        WinCheckTo()
        if(WinCheck == 1 ):
            print("Stop")
            break
        elif(GameProcess == "Stop"):
            break
