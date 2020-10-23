# Imports =
from Functions import *
from socket import *

#  Host IP and Host port initialization
HOST = '127.0.0.1'
PORT = 4444

#  Board Initialization
board_raw = [
  #  Comes Second
  #  0  1  2
    [0, 0, 0],  # 0
    [0, 0, 0],  # 1  Comes First
    [0, 0, 0],  # 2
]

#  var initialization
win_p1 = False
win_p2 = False
player_1 = True

#  Prints board once at the start of the game
print(print_board(board_raw))

#  Main game loop
with socket(AF_INET, SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        while not win_p1 or win_p2:
            #  Player 1's turn
            if player_1:
                try:
                    #  Coord input
                    turn = input('1) Please enter a two digit number, with the row number first, and the column number last:\n')
                    #  Places X on board
                    if board_raw[int(turn[0])][int(turn[1])] == 0:
                        board_raw[int(turn[0])][int(turn[1])] = -1
                    else:
                        print("Space is not empty. Try again")
                        continue
                    #  Prints board after X is placed
                    print(print_board(board_raw))
                    # Checks to see if that move was a winning move
                    win_p1 = win_condition1(board_raw)
                    #  Changes turn to player 2
                    player_1 = False
                    continue
                # Error catching in case of invalid coord input
                except IndexError:
                    print("Oops! Looks like we couldn't figure out what space you wanted to place your O. Please try again")
                    continue
            #  Player 2's turn
            elif not player_1:
                try:
                    #  Coord input
                    turn = input('2) Please enter a two digit number, with the row number first, and the column number last:\n')
                    #  Places O on board
                    if board_raw[int(turn[0])][int(turn[1])] == 0:
                        board_raw[int(turn[0])][int(turn[1])] = 1
                    else:
                        print("Space is not empty. Try again")
                        continue
                    #  Prints board after O is placed
                    print(print_board(board_raw))
                    # Checks to see if that move was a winning move
                    win_p2 = win_condition2(board_raw)
                    #  Changes turn to player 2
                    player_1 = True
                    continue
                # Error catching in case of invalid coord input
                except IndexError:
                    print("Oops! Looks like we couldn't figure out what space you wanted to place your O. Please try again")
                    continue

        #  Figure out which player wins, and print win message
        if win_p1:
            print('PLAYER 1 WINS')
        if win_p2:
            print('PLAYER 2 WINS')