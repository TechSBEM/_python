# Displaying User Information


position_col = int(input("Enter col(1-3): ")) -1
position_row = int(input('Enter Row(1-3): '))-1


row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']
gameboard = [row1, row2,row3]

def take_input(col,row ):
    # out of bounds
    if col not in range(3) or row not in range(3):
        return "Number out of range"

    gameboard[col][row]= 'X'

    print(gameboard[0])
    print(gameboard[1])
    print(gameboard[2])





print(take_input(position_col, position_row))