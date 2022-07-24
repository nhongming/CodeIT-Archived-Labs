'''
    Tic Tac Toe (Easy)
        - In this problem you will create a tictactoe simulator 
        - We have initialized a 2d list board for you
        - The numbers 1 to 9 mark each position on the board
        - To make a move on the board, a player has to simply input the position's number 

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

        Note: Write your code in the main function
'''


def printBoard(board):
    print()
    for row in range(len(board)):
        for col in range(len(board[0])):
            print(board[row][col], end=" ")
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


def makeMove(player, board):
    move = input("{}'s turn: ".format(player))
    moveRow = getRowCol(move)[0]
    moveCol = getRowCol(move)[1]

    while (board[moveRow][moveCol] == 'O' or board[moveRow][moveCol] == 'X'):
        move = int(input("invalid move, {}'s turn: ".format(player)))
        moveRow = int((move - 1) / 3)
        moveCol = (move - 1) % 3

    board[moveRow][moveCol] = player
    return

'''
    getRowCol: 
        - Takes in a move as a string 
        - Returns a list where the first element is the row and second is the column of that move on the board. Example: getRowCol("6") -> [1, 3]
        - You can use the row and col received to index into the board and change that value
'''
def getRowCol(move):
    move = int(move)
    moveRow = int((move - 1) / 3)
    moveCol = (move - 1) % 3
    return [moveRow, moveCol]

def main():
    '''
        board: 
            - You are given a 2D list called board which contains the numbers "1" to "9" in strings
            - These represent the positions on the tic tac toe board!
    '''

    board = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']
    ]

    # WRITE YOUR CODE HERE
    winnerExists = False
    for i in range(9):
        if i % 2 == 0:
            printBoard(board)
            makeMove("O", board)
            if (isDiagonal(board) or isRow(board) or isCol(board)):
                winnerExists = True
                break
        else:
            printBoard(board)
            makeMove("X", board)
            if (isDiagonal(board) or isRow(board) or isCol(board)):
                winnerExists = True
                break

    if not winnerExists:
        print("no winner")

if __name__ == '__main__':
    main()