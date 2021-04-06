#importing OS module to clear terminal
import os

#function to clear the terminal
def clear():
    os.system('cls')

#function to clear any items currently being displayed
#& to print the current status of the board
def print_board(a, b, c):
    clear()
    print(c)
    print(b)
    print(a)
    print("\n")



#function to start the current player's turn
def player_turn(a, b, c, single_list, player):

    while True:
            #ask the player for a number 1-9. each number corresponding to a space on the board
            #e.g board and number relation
            #  7| 8 |9
            # ----------
            #  6| 5 |4
            # ----------
            #  1| 2 |3
            try:
                player_choice = int(input(f"{player}: Please select a number (1-9): "))
                #if the player input is not the range of 1 - 9. Ask againa and specify range.
                if player_choice not in range(1, 10):
                    print("Please select a number between 1 and 9.")
                    continue
            except:
                #if the player input is not a number and an error occurs, ask for input again
                continue
            else:
                #if the designated space is empty, place the user's choice
                if not single_list[player_choice-1]:
                    single_list[player_choice-1] = player
                    update_board(a,b,c, single_list)

                    #return the opposite player
                    if player == 'O':
                        return 'X'
                    else:
                        return 'O'
                    print('\n')
                else: #if the space selected already has a value, alert user to select a different space
                    print("Space selected is already in use.")
                    continue


#function that updates the 3x3 board with the values from the single list
def update_board(a,b,c, single_list):

    a[0] = single_list[0]
    a[1] = single_list[1]
    a[2] = single_list[2]

    b[0] = single_list[3]
    b[1] = single_list[4]
    b[2] = single_list[5]

    c[0] = single_list[6]
    c[1] = single_list[7]
    c[2] = single_list[8]

    print_board(a, b, c)


#function to check all possible combinations for a Win

def check_board(a,b,c, player):
    #
    if player == "O":
        player = "X"
    elif player == "X":
        player = "O"

    if a[0] == b[0] == c[0] == player.upper():
        print(f"{player} is the winner!")
        return True
    elif a[1] == b[1] == c[1] == player.upper():
        print(f"{player} is the winner!")
        print("Winner")
        return True
    elif a[1] == b[1] == c[1] == player.upper():
        print(f"{player} is the winner!")
        return True
    elif a[2] == b[2] == c[2] == player.upper():
        print(f"{player} is the winner!")
        return True
    elif a[0] == a[1] == a[2] == player.upper():
        print(f"{player} is the winner!")
        return True
    elif b[0] == b[1] == b[2] == player.upper():
        print("Winner")
        return True
    elif c[0] == c[1] == c[2] == player.upper():
        print(f"{player} is the winner!")
        return True
    elif a[0] == b[1] == c[2] == player.upper():
        print(f"{player} is the winner!")
        return True
    elif a[0] == b[1] == c[2] == player.upper():
        print(f"{player} is the winner!")
        return True
    elif a[2] == b[1] == c[0] == player.upper():
        print(f"{player} is the winner!")
        return True
    elif a[0] and a[1] and a[2] and b[0] and b[1] and b[2] and c[0] and c[1] and c[2]:
         #if all squares are filled and no win; end game
        print("Draw!")
        return True
    else:
        return False


#ask the user if they'd like to start a new game
def start_game(game_on):
    while True:
        game_on = input("Would you like to start a new game? (Y/N): ")

        if game_on[0].upper() == "Y" or game_on[0].upper() == "N":
            return game_on
        else:
            print("Please utilize Y or N.")


#program variables
#rows to assign values toward and print the board
row_1 = [" ", " ", " "]
row_2 = [" ", " ", " "]
row_3 = [" ", " ", " "]
#a single list to assign values toward
single_list = ["", "", "", "", "", "", "", "", ""]
#starting player is O
player = 'O'
#value designates whether to continue the game or not
game_on = ''

#start of game
print("Welcome to Tic Tac Toe")
print("\n")

#asking the user to start a new game
game_on = start_game(game_on)

#if yes, begin game
while game_on[0].upper() == "Y":

    #print current board
    print_board(row_1, row_2, row_3)

    #ask current player to play their turn
    player = player_turn(row_1, row_2, row_3, single_list, player)

    #check if the player who just played has won
    winner = check_board(row_1, row_2, row_3, player)

    #if there is a winner ask the user if they'd like a new game
    #if so, clear the board & update the board
    if winner:
        #game_on = input("Would you like to start another game? (Y/N): ")
        game_on = start_game(game_on)
        single_list = ["", "", "", "", "", "", "", "", ""]
        update_board(row_1, row_2, row_3, single_list)

#if no, close out the game and thank the players
clear()
print("\n")
print('Thank you for playing!')
