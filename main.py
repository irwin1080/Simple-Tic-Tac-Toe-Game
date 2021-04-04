from IPython.display import clear_output

def print_board(a, b, c):
    #from IPython.display import clear_output
    clear_output()
    print(c)
    print(b)
    print(a)
    print("\n")



def player_turn(a, b, c, single_list, player):
    if player.upper() == 'X':
        player_choice = int(input("X: Please select a number (1-9): "))
        if player_choice not in range(1, 10):
            print("Please select a number between 1 and 9.")
            player_turn(a, b, c, single_list, player)
            return

        #if the string is empty; assign player to list place
        if not single_list[player_choice-1]:
            single_list[player_choice-1] = player
            update_board(a,b,c, single_list)
            return 'O'
            print('\n')
        else: #if it is not empty, redo and ask ask again
            player_turn(a, b, c, single_list, player)
    elif player.upper() == 'O':
        player_choice = int(input("O: Please select a number (1-9): "))
        if player_choice not in range(1, 10):
            print("Please select a number between 1 and 9.")
            player_turn(a, b, c, single_list, player)
            return

        #if the string is empty; assign player to list place
        if not single_list[player_choice-1]:
            single_list[player_choice-1] = player
            update_board(a,b,c, single_list)
            return 'X'
            print('\n')
        else: #if it is not empty, redo and ask ask again
            player_turn(a, b, c, single_list, player)


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

def check_board(a,b,c, player):
    if player == "O":
        player = "X"
    elif player == "X":
        player = "O"

    if a[0] == b[0] == c[0] == player.upper():
        print("Winner")
        return True
    elif a[1] == b[1] == c[1] == player.upper():
        print("Winner")
        return True
    elif a[1] == b[1] == c[1] == player.upper():
        print("Winner")
        return True
    elif a[2] == b[2] == c[2] == player.upper():
        print("Winner")
        return True
    elif a[0] == a[1] == a[2] == player.upper():
        print("Winner")
        return True
    elif b[0] == b[1] == b[2] == player.upper():
        print("Winner")
        return True
    elif c[0] == c[1] == c[2] == player.upper():
        print("Winner")
        return True
    elif a[0] == b[1] == c[2] == player.upper():
        print("Winner")
        return True
    elif a[0] == b[1] == c[2] == player.upper():
        print("Winner")
        return True
    elif a[2] == b[1] == c[0] == player.upper():
        print("Winner")
        return True

     #edge case: if all squares are filled and no win; end game
    if a[0] and a[1] and a[2] and b[0] and b[1] and b[2] and c[0] and c[1] and c[2]:
        print("Draw!")
        return True



row_1 = [" ", " ", " "]
row_2 = [" ", " ", " "]
row_3 = [" ", " ", " "]
single_list = ["", "", "", "", "", "", "", "", ""]
player = 'O'

print("Welcome to Tic Tac Toe")
print("\n")

game_on = input("Would you like to start a game? (Y/N): ")

while game_on.upper() == "Y":

    print_board(row_1, row_2, row_3)

    player = player_turn(row_1, row_2, row_3, single_list, player)

    winner = check_board(row_1, row_2, row_3, player)

    if winner:
        game_on = input("Would you like to start another game? (Y/N): ")
        single_list = ["", "", "", "", "", "", "", "", ""]

clear_output()
print("\n")
print('Thank you for playing!')
