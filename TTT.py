b='''
          |    |
     -----------------
          |    |
     -----------------
          |    |
     '''
"""
     sampleBoard=[[1,2,3],[4,5,6],[7,8,9]]
     print(sampleBoard)
     for row in range(len(sampleBoard)):    #range(len(sampleBoard))->[0,1,2]
          for columns in range(len(sampleBoard[row])):
               print(sampleBoard[row][columns])
"""
def printBoard(board):
     for r in range(3):
          print(board[r][0]+"|"+board[r][1]+"|"+board[r][2])
          if r<2:
               print("-"*5)

#returns a true or false value on whether we can choose that spot
def chooseSpot(r,c,symbol,board):
     #if the spot is open
     if board[r][c] == " ":
          #add the symbol and return true
          board[r][c]=symbol
          return True    
     return False

def catGame(board):
     #check every spot to see if there is something
     for row in range(len(board)):    #range(len(sampleBoard))->[0,1,2]
          for columns in range(len(board[row])):
               if (board[row][columns]) == " ":
                    return False
     print("CAT GAME!")
     return True         #return stop the function and give a value back

def checkForWinners(board):
     #check horizontally
     for r in range(len(board)):
          #r is the rows and the columns are the same for each row
          if (board[r][0] == board[r][1] and board[r][1] == board[r][2]) and board[r][0]!=" ":
               print("Winner winner Turkey dinner!")
               printBoard(board)
               return True

     #check vertically
     for c in range(len(board)):
          #r is the rows and the columns are the same for each row
          if (board[0][c] == board[1][c] and board[1][c] == board[2][c]) and board[0][c]!=" ":
               print("Winner winner Turkey dinner!")
               printBoard(board)
               return True

     #check diagonally
     #hard code

board=[[" "," "," "],[" "," "," "],[" "," "," "]]
symbol="X"
while symbol!="Q":
     printBoard(board)

     #if the symbol is x
     # then run the code already built
     #else
     # run the computer's code

     #loop until a good spot is chosen
     goodSpot=False
     while not goodSpot:
          r = int(input("row: "))-1
          c = int(input("col: "))-1
          #if we can NOT choose the spot
          if((0<=r<=2) and (0<=c<=2)):
               if (not chooseSpot(r,c,symbol,board)):
                    print("Spot Taken")
               else:
                    goodSpot = True
     
     #check for a winner or CAT
     if catGame(board) or checkForWinners(board):
          symbol="Q"
     #switching our symbols
     if symbol=="X":
          symbol="O"
     elif symbol=="O":
          symbol="X"



