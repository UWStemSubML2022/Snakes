# import all of the libaries you need at the top of the file
# you may need to add more libraries to this list
import numpy as np
import random

# Write a function that prints your board based on a 
# an array of how  the board is currently populated
# This function does not need to return anything.
def print_board(board_array):
    print("Printing board")

# Write a function that creates a blank array of the 
# correct size and shape to represent your board.
# This function should return the array or the blank board.
def init_board():
    print("Initializing a new board")

    return 0 # placeholder

# Write a function that allows one player to take their entire turn.
# It should return the new version of the board.
def take_turn(current_character, board):
    print("Starting turn")

    # You will need to collect the  players move in the form 
    # of command line input
    move = 0 # placeholder for player's move input

    # check if the move is valid
    while not valid_move(int(move), board):
        # If the move is invalid, try to collect valid input
        break #This will need to be removed. It is just there to stop the infinite loop

    # update board
    update_board(current_character, int(move), board)

    return 0 # placeholder

# You will need to take the  current player, their move choice, 
# and the current board and determine how the board should be updated 
# This function should return the updated board array
def update_board(player, move, board):
    print("Updating the board")

    return 0 # placeholder

# You will need to determine which player will start the game. 
# This is less important with human player, but will become important 
# when playing against computers or having the computers play against 
# themselves. 
# This function should return the starting player
def determine_start():
    print("Determining the start of the game")

    return 0 # placeholder

# You will need to determine if the players move is valid. This should 
# include checking that the move is within the bounds of the board and 
# that the board is still open in that position
# This function should return a boolean (True or False)
def valid_move(move, board):
    print("Checking if the move is valid")

    return 0 # placeholder

# You will need to determine if the players move has won the game. You 
# should dewtermine what creates a winning move in your game and check 
# for all of those possibilities. You will likely want to create multiple 
# functions to do this like we did with check_rows(), check_columns(), 
# and check_diagonals() in class
# This function should return a boolean (True or False)
def check_win(character, board):
    print("Checking if the game has been won") 

    return 0 # placeholder

# This function should check whose turn it currently is and change it 
# to the other player 
# This function should return a character or integer
def switch_player(character):
    print("Switching player")

    return 0 # placeholder

# This function serves as your main function, where you can call all 
# of the other functions in the proper order and check if the game 
# should be restarted
#This function should not return anything
def play_game():
    print("Entering play game")

    # declare the board options
    board_options = np.array([['0', '1', '2'],
                              ['3', '4', '5'],
                              ['6', '7', '8']])

    # print the board options
    print_board(board_options)

    # initialize the board
    board = init_board()

    # keep track of if the game has been won
    win = False

    # determine how the game will be started
    player = determine_start()

    # while the game has not been won stay inside of a loop
    while not win:
        # take turns
        take_turn(player, board)

        # print the board after each turn
        print_board(board)

        # check if the  game has been won after each turn
        if check_win(player, board):
            # if the game has been won, ask if they would like to play again
            again = input("Would you like to play again? [Y/N]")

            # if they would like to play again...
            if (again == 'Y') or (again == 'y'):
                # reset the board
                print("Resetting board")
                board = init_board()

                # determine how the game will be started
                player = determine_start()

            # if they would not like to play again...
            elif (again == 'N') or (again == 'n'):
                # exit the program
                print("Thanks for playing!")
                exit(0)

        # swap which players turn it is at the end of each turn
        player = switch_player(player)

        exit(0)


if __name__ == "__main__":
    play_game()

