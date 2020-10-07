from random import randrange
win = False
board = [[1,2,3],[4,'X',6],[7,8,9]]
def DisplayBoard(board):
#
# the function accepts one parameter containing the board's current status
# and prints it out to the console
#
    for i in board:
        print(('+'+'-'*7)*3+'+')
        print(('|'+' '*7)*3+'|')
        for j in range(len(i)):
            print('|'+' '*3+str(i[j])+' '*3, end='')
        print('|')
        print(('|'+' '*7)*3+'|')
    print(('+'+'-'*7)*3+'+')

def IsMoveOutOfRange(move):
    while move<1 or move>9:
        move = int(float(input('The number must be in range <1,9>. Enter your move again: ')))
    return move
    
def IsMoveOnBoard(move):
    freeFields = MakeListOfFreeFields(board)
    for i in range(len(freeFields)):
        if board[freeFields[i][0]][freeFields[i][1]]==move:
            global row
            row = freeFields[i][0]
            global column
            column = freeFields[i][1]
            return False
    return True 

def MakeListOfFreeFields(board):
#
# the function browses the board and builds a list of all the free squares; 
# the list consists of tuples, while each tuple is a pair of row and column numbers
#
    freeSquares = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]=='X' or board[i][j]=='O':
                continue
            freeSquares.append((i,j))
    return freeSquares

def EnterMove(board):
#
# the function accepts the board current status, asks the user about their move, 
# checks the input and updates the board according to the user's decision
#
    move = int(float(input('Enter your move: ')))
    move = IsMoveOutOfRange(move)
    while IsMoveOnBoard(move):
        move = IsMoveOutOfRange(int(float(input('This field is occupied. Enter your move again: '))))
    board[row][column]= sign = 'O'
    DisplayBoard(board)
    return sign

def VictoryFor(board, sign):
#
# the function analyzes the board status in order to check if 
# the player using 'O's or 'X's has won the game
#
    win = False
    areAnyMovesLeft = MakeListOfFreeFields(board)
    if not win:
        j=1
        for i in range(len(board)):     # checking horizontal winning sets
            if board[i][j-1]==board[i][j]==board[i][j+1]:
                win = True
                break
    
        i=1
        j = 0
        for j in range(len(board)):     # checking vertical winning sets
            if board[i-1][j]==board[i][j]==board[i+1][j]:
                win = True
                break
        
        i = j = len(board)//2            # middle position
        if board[i][j]==board[i-1][j-1]==board[i+1][j+1]:   #checking \ winning set
            win = True
        
        if board[i][j]==board[i-1][j+1]==board[i+1][j-1]:   #checking / winning set
            win = True
            
        if not win and not areAnyMovesLeft:
            print('It seems we have a tie here.')
            win = True #only to avoid asking for inputting number after finishing the game
            return win
    if win:
        if sign=='X':
            print('You lost :( Maybe next time...')
        else:
            print('Congratulations! You won!')
    return win
            
def DrawMove(board):
#
# the function draws the computer's move and updates the board
#
    move = randrange(10)
    while IsMoveOnBoard(move):
        move = randrange(10)
    print(move)
    board[row][column]= sign = 'X'
    DisplayBoard(board)
    return sign

DisplayBoard(board)
while not win:
    win = VictoryFor(board,EnterMove(board))
    if not win:
        win = VictoryFor(board,DrawMove(board))
