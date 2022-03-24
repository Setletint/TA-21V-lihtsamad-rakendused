from array import array
from ast import Call


gameboard = [
  ".",".",".",
  ".",".",".",
  ".",".","."
  ]

def CallGame():
  print(gameboard[0], gameboard[1], gameboard[2])
  print(gameboard[3], gameboard[4], gameboard[5])
  print(gameboard[6], gameboard[7], gameboard[8])
CallGame()

mark_pos = int(input("Choose position: "))

if(mark_pos == 1):
  gameboard[0] = "X"
  CallGame()
if(mark_pos == 2):
  gameboard[1] = "X"
  CallGame()
