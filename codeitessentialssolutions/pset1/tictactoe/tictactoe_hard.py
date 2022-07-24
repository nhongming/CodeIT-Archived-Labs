'''
    Tic Tac Toe (Hard)
        - In this problem you will create a tictactoe simulator for an n x n size board
        - You are taking in n (no. of rows  / cols in the board) as a command line argument
        - We have then created a function (generateBoard) which returns a n x n board as a 2d list for you
        - The numbers 1 to n^2 mark each position on the board
        - To make a move on the board, a player has to simply input the position's number
        - A win condition for an n x n board is such that a player 
          has marked n positions on the board in a vertical, horizontal or diagonal
          (e.g. for a 4 x 4 board, positions 1, 2, 3, 4 are marked by player O)
        
    Your Tasks:
		1. For each player (O & X):
            - Print the board
            - Ask the user which position he would like to make his move on
            - Check whether that position is valid:
                -> This means that the position has not been taken already
                -> Note: You may assume that the users will only input a number from 1 - 9
            - Change that position on the list to be the player. E.g. if 'O' inputs 1, board[0][0] should now be 'O'

		2. Repeat until a win condition is found, or all positions have been taken
            - If a winner is found, print "winner: <player symbol>" in this exact format (e.g. "winner: O")
            - If there is no winner, print "no winner", in this exact format
            - Your program should work for any board size
'''


from sys import argv
'''
    generateBoard:
        - This function takes in n (no. of rows / cols for the board)
        - It then returns an n x n board as a 2d list, where each position is marked from 1 to n^2
'''
def generateBoard(n):
    board = [['0'for j in range(n)] for i in range(n)]
    counter = 1
    for i in range(n):
        for j in range(n):
            board[i][j] = str(counter)
            counter += 1

    return board

'''
    getRowCol: 
        - Takes in a move as a string 
        - Returns a list where the first element is the row and second is the column of that move on the board. Example: getRowCol("6") -> [1, 3]
        - You can use the row and col received to index into the board and change that value
'''
def getRowCol(move, n):
    move = int(move)
    moveRow = int((move - 1) / n)
    moveCol = (move - 1) % n
    return [moveRow, moveCol]

def printBoard(board):
    print()
    for row in range(len(board)):
        for col in range(len(board[0])):
            print(board[row][col], end=" " * (3 - len(board[row][col])))
        print()
    print()
    return


def isRow(board):
    for i in range(len(board)):
        potentialWinner = board[i][0]
        hasWon = True
        for j in range(1, len(board[i])):
            if potentialWinner != board[i][j]:
                hasWon = False
                break
        if hasWon:
            printBoard(board)
            print("winner: {}".format(potentialWinner))
            return True
    return False


def isCol(board):
    for j in range(len(board[0])):
        potentialWinner = board[0][j]
        hasWon = True
        for i in range(1, len(board)):
            if potentialWinner != board[i][j]:
                hasWon = False
                break
        if hasWon:
            printBoard(board)
            print("winner: {}".format(potentialWinner))
            return True
    return False


def checkDiagonal(board):
    potentialWinner1 = board[0][0]
    hasWon = True
    for i in range(1, len(board)):
        if potentialWinner1 != board[i][i]:
            hasWon = False
            break
    if hasWon:
        return potentialWinner1

    potentialWinner2 = board[0][len(board[0]) - 1]
    hasWon = True
    for i in range(1, len(board)):
        j = len(board[0]) - 1 - i
        if potentialWinner2 != board[i][j]:
            hasWon = False
            break
    if hasWon:
        return potentialWinner2

    return None


def isDiagonal(board):
    result = checkDiagonal(board)
    if result != None:
        printBoard(board)
        print("winner: {}".format(result))
        return True
    else:
        return False


def makeMove(player, board, n):
    move = input("{}'s turn: ".format(player))
    rowCol = getRowCol(move, n)
    moveRow = rowCol[0]
    moveCol = rowCol[1]

    while (board[moveRow][moveCol] == 'O' or board[moveRow][moveCol] == 'X'):
        move = int(input("invalid move, {}'s turn: ".format(player)))
        rowCol = getRowCol(move, n)
        moveRow = rowCol[0]
        moveCol = rowCol[1]

    board[moveRow][moveCol] = player
    return




def main():
    if len(argv) != 2:
        print('Usage: python tictactoe.py <board-size n>')
        exit()

    n = int(argv[1])

    board = generateBoard(n)

    # WRITE YOUR CODE HERE
    winnerExists = False
    for i in range(n ** 2):
        if i % 2 == 0:
            printBoard(board)
            makeMove("O", board, n)
            if (isRow(board) or isDiagonal(board) or isCol(board)):
                winnerExists = True
                break
        else:
            printBoard(board)
            makeMove("X", board, n)
            if (isRow(board) or isDiagonal(board) or isCol(board)):
                winnerExists = True
                break

    if not winnerExists:
        printBoard(board)
        print("no winner")


if __name__ == '__main__':
    main()
