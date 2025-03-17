# game_list = [1, 2, 3]


def display_game(game_list):
    print("Here is the current list:")
    print(f'{game_list} \n')
    # return game_list


def position_choice():
    choice = 'wrong'
    while choice not in ['1', '2', '2']:
        choice = input("\nEnter a number (1-3): ")
        if choice not in ['1', '2', '3']:
            print('Invalid number, Number should be in range (1-3)')
    return int(choice)

# print( dispay_game(game_list))
# print(position_choice())



def replacement_choice(game_list, position):
    user_placement =input('THe a string to a place at position: ')
    game_list[position] = user_placement
    return game_list



# print(replacement_choice(game_list, 1))


def gameon_choice():
    choice= 'wrong'

    while choice not in ['Y', 'N']:
        choice = input('Keep playing? (Y or N) ')

        if choice not in ['Y', 'N']:
            print('Sorry, I dont understand, please choose Y or N ')

    if choice == 'Y':
        return True
    else:
        return False


game_on = True
game_list = [1, 2, 3]

while game_on:
    # Displaying the intial gamelist
    display_game(game_list)
    #Choicing your prefered postion in the famelist
    position = position_choice()
    #Replacing the choosen position with your typed string
    game_list=replacement_choice(game_list,position)
    #Displaying the new gamelist
    display_game(game_list)
    #Asking the user whether he wants to continue or not
    game_on = gameon_choice()

