import os
BLACK  = "\033[30m"
RED    = "\033[31m"
GREEN  = "\033[32m"
YELLOW = "\033[33m"
BLUE   = "\033[34m"
PURPLE = "\033[35m"
CYAN   = "\033[36m"
WHITE  = "\033[37m"
RESET  = "\033[0m"

board = ["  1", "| 2 |", "3  ", "  4", "| 5 |", "6  ", "  7", "| 8 |", "9  "]
check = [0, 0, 0, 0, 0, 0, 0, 0, 0]

def clear_console():
    # Clear the terminal screen based on the OS.
    if os.name == 'nt':
        os.system('cls')  # Windows
    else:
        os.system('clear')  # Unix/Linux
    # print("FAKE CLEAR")


def printboard():
  clear_console()
  print(board[0], board[1], board[2])
  print(" ----------- ")
  print(board[3], board[4], board[5])
  print(" ----------- ")
  print(board[6], board[7], board[8])

def clear():
  global board
  global check
  board = ["  1", "| 2 |", "3  ", "  4", "| 5 |", "6  ", "  7", "| 8 |", "9  "]
  check = [0, 0, 0, 0, 0, 0, 0, 0, 0]
  print("\033[31m"+"\nNEW GAME!"+"\033[0m")

def x():
  place = input("\033[34m"+"\nEnter a number for X: "+"\033[0m")
  print("\n")
  place = int(place)-1
  if check[place] == 1 or check[place] ==2:
    print("This place is already taken. Please choose another place.")
    x()
  else:
    if place == 1 or place == 4 or place == 7:
      board[place] = BLUE+"| X |"+RESET
      check[place] = 1
    elif place == 0 or place == 3 or place == 6:
      board[place] = BLUE+"  X"+RESET
      check[place] = 1
    else:
      board[place] = BLUE+"X  "+RESET
      check[place] = 1

def o():
  place = input("\033[34m"+"\nEnter a number for O: "+"\033[0m")
  print("\n")
  place = int(place)-1
  if check[place] == 1 or check[place] ==2:
    print("This place is already taken. Please choose another place.")
    o()
  else:
    if place == 1 or place == 4 or place == 7:
      board[place] = BLUE+"| O |"+RESET
      check[place] = 2
    elif place == 0 or place == 3 or place == 6:
      board[place] = BLUE+"  O"+RESET
      check[place] = 2
    else:
      board[place] = BLUE+"O  "+RESET
      check[place] = 2

def xwin():
  print("\033[32m"+"\nX wins!"+"\033[0m")
  clear()

def owin():
  print("\033[32m"+"\nO wins!"+"\033[0m")
  clear()
  
def checkwin():
  #rows
  # row 1 x
  if check[0] == 1 and check[1] == 1 and check[2] == 1:
    xwin()
  # row 1 o
  elif check[0] == 2 and check[1] == 2 and check[2] == 2:
    owin()
  # row 2 x
  elif check[3] == 1 and check[4] == 1 and check[5] == 1:
    xwin()
  # row 2 o
  elif check[3] == 2 and check[4] == 2 and check[5] == 2:
    owin()
  # row 3 x
  elif check[6] == 1 and check[7] == 1 and check[8] == 1:
    xwin()
  # row 3 o
  elif check[6] == 2 and check[7] == 2 and check[8] == 2:
    owin()
  #columns
  # column 1 x
  elif check[0] == 1 and check[3] == 1 and check[6] == 1:
    xwin()
  # column 1 o
  elif check[0] == 2 and check[3] == 2 and check[6] == 2:
    owin()
  # column 2 x
  elif check[1] == 1 and check[4] == 1 and check[7] == 1:
    xwin()
  # column 2 o
  elif check[1] == 2 and check[4] == 2 and check[7] == 2:
    owin()
  # column 3 x
  elif check[2] == 1 and check[5] == 1 and check[8] == 1:
    xwin()
  # column 3 o
  elif check[2] == 2 and check[5] == 2 and check[8] == 2:
    owin()
  #diagonals
  # diagonal 1 x
  elif check[0] == 1 and check[4] == 1 and check[8] == 1:
    xwin()
  # diagonal 1 o
  elif check[0] == 2 and check[4] == 2 and check[8] == 2:
    owin()
  # diagonal 2 x
  elif check[2] == 1 and check[4] == 1 and check[6] == 1:
    xwin()
  # diagonal 2 o
  elif check[2] == 2 and check[4] == 2 and check[6] == 2:
    owin()
  else:
    print("")

    

printboard()
while True:
  x()
  printboard()
  checkwin()
  o()
  printboard()
  checkwin()
