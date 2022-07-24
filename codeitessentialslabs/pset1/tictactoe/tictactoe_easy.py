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


'''
    getRowCol: 
        - Takes in a move as a string 
        - Returns a list where the first element is the row and second is the column of that move on the board. Example: getRowCol("6") -> [1, 2]
        - You can use the row and col received to index into the board and change that value
'''
from turtle import position


def getRowCol(move):
    move = int(move)
    moveRow = int((move - 1) / 3)
    moveCol = (move - 1) % 3
    return [moveRow, moveCol]

'''
    function to display the board (3 by 3 board representation) using indexing
'''
def display_board(board):
    print(end="\n")
    print(board[0][0] + board[0][1] + board[0][2])
    print(board[1][0] + board[1][1] + board[1][2])
    print(board[2][0] + board[2][1] + board[2][2])

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

'''
    a function that takes in a board and checks to see if the player has won using Boolean check.

'''
def win_check(board,marker):

    return ((board[0][0] == marker and board[0][1] == marker and board[0][2] == marker) or # across the top
    (board[1][0] == marker and board[1][1] == marker and board[1][2] == marker) or # across the middle
    (board[2][0] == marker and board[2][1] == marker and board[2][2] == marker) or # across the bottom
    (board[0][0] == marker and board[1][0] == marker and board[2][0] == marker) or # down the left side
    (board[0][1] == marker and board[1][1] == marker and board[2][1] == marker) or # down the middle
    (board[0][2] == marker and board[1][2] == marker and board[2][2] == marker) or # down the right side
    (board[2][0] == marker and board[1][1] == marker and board[0][2] == marker) or # diagonal left to right
    (board[2][2] == marker and board[1][1] == marker and board[0][0] == marker))    # diagonal right to left 

'''
    a function that uses the random module to randomly decide which player goes first.
'''
from random import randint

def choose_first():
    if randint(0,1) == 0:
        return 'Player 2'
    return 'Player 1'

'''
    a function that returns a boolean indicating whether a move on the board is freely available.
    Therefore can determine whether that position is valid
    if invalid, ask again until a valid answer is given.
'''
def move_check(board,position):

    marker_position = getRowCol(position)
    row_marker = marker_position[0]
    col_marker = marker_position[1]

    return ( board[row_marker][col_marker] in ['O', 'X'] )

'''
    a function that checks if the board is full and returns a boolean value. True if full, False otherwise.
'''
def full_board_check(board,position,marker):

    for position in ['1','2','3','4','5','6','7','8','9']:
        if move_check(board,position) == False:
            return False
    return True
'''
    a function that asks for a player's next position (as a number 1-9)
    using move_check(board, position) to check if its a free position. 
    If it is, then return the position for later use.
'''

def player_choice(board,marker):

    position = input("\n{}'s turn: ".format(marker))
    while ( position not in ['1','2','3','4','5','6','7','8','9'] ) or ( move_check(board, position) == True ):
        position = input("invalid move, {}'s turn: ".format(marker))
    return position

def replay():
	
	return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

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

    while True:

        game_board = board.copy()
        player1_marker, player2_marker = player_input()
        turn = choose_first()
        print("{} will go first.".format(turn))

        game_launcher = input("Are you ready to play? Enter 'Y' or 'N'.")

        if game_launcher.lower() == 'y':
            game_on = True
        else:
            game_on = False

        while game_on == True:

            if turn == 'Player 1':
                # Player1's turn
                display_board(game_board)
                position = player_choice(game_board, player1_marker)
                place_marker(game_board, player1_marker, position)

                if win_check(game_board, player1_marker):
                    display_board(game_board)
                    print("\nwinner: {}".format(player1_marker))
                    game_on = False
                    break

                else: 

                    if full_board_check(game_board,position,player1_marker):
                        display_board(game_board)
                        print("\nno winner")
                        game_on = False
                        break
                    else:
                        turn = 'Player 2'
                        
            else:
                # Player2's turn
                display_board(game_board)
                position = player_choice(game_board, player2_marker)
                place_marker(game_board, player2_marker, position)

                if win_check(game_board, player2_marker):
                    display_board(game_board)
                    print("\nwinner: {}".format(player2_marker))
                    game_on = False
                    break

                else: 

                    if full_board_check(game_board,position,player2_marker):
                        display_board(game_board)
                        print("\nno winner")
                        game_on = False
                        break
                    else:
                        turn = 'Player 1'
                            
        
        if not replay():
            break

if __name__ == '__main__':
    main()