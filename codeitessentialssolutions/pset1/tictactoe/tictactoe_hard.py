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


def main():
    if len(argv) != 2:
        print('Usage: python tictactoe.py <board-size n>')
        exit()

    n = int(argv[1])

    board = generateBoard(n)

    # WRITE YOUR CODE HERE

    '''
        function to display the board (n by n board representation) using iterations
    '''
    def display_board(board):
        print(end="\n")
        for move_row in board:
            for move_col in move_row:
                print(move_col, end="")
            print(end="\n")
    '''
        testing displaying the n by n board
    '''
        # display_board(board)

    '''
        a function that can take in a player input and assign their marker as 'X' or 'O'.

    '''
    def player_input():

        marker = ''

        while not ( marker == 'X' or marker == 'O' ):
            marker = input('Player 1: Do you want to be X or O? ').upper()
        if marker == 'X':
            return ('X','O')
        else:
            return ('O','X')
        
    '''
        function that takes in the board list object, a marker ('X' or 'O'), 
        and a desired position (number 1-9) and assigns it to the board.
    '''
    def place_marker(board, marker, position):

        rowmarker = getRowCol(position)

        row_position = rowmarker[0]

        col_position = rowmarker[1]        

        board[row_position][col_position] = marker


if __name__ == '__main__':
    main()
