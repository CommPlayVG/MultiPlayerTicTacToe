
#  Conditions that player 1 wins
def win_condition1(raw):
    win1 = False
    #  vertical wins
    if raw[0][0] == -1 and raw[1][0] == -1 and raw[2][0] == -1:
        win1 = True
    elif raw[0][1] == -1 and raw[1][1] == -1 and raw[2][1] == -1:
        win1 = True
    elif raw[0][2] == -1 and raw[1][2] == -1 and raw[2][2] == -1:
        win1 = True
    #  Horizontal wins
    elif raw[0][0] == -1 and raw[0][1] == -1 and raw[0][2] == -1:
        win1 = True
    elif raw[1][0] == -1 and raw[1][1] == -1 and raw[1][2] == -1:
        win1 = True
    elif raw[2][0] == -1 and raw[2][1] == -1 and raw[2][2] == -1:
        win1 = True
    #  Diagonal wins
    elif raw[0][0] == -1 and raw[1][1] == -1 and raw[2][2] == -1:
        win1 = True
    elif raw[0][2] == -1 and raw[1][1] == -1 and raw[2][0] == -1:
        win1 = True
    else:
        win1 = False
    return win1


# Conditions that player 2 wins
def win_condition2(raw):
    win2 = False
    #  vertical wins
    if raw[0][0] == 1 and raw[1][0] == 1 and raw[2][0] == 1:
        win2 = True
    elif raw[0][1] == 1 and raw[1][1] == 1 and raw[2][1] == 1:
        win2= True
    elif raw[0][2] == 1 and raw[1][2] == 1 and raw[2][2] == 1:
        win2= True
    #  Horizontal wins
    elif raw[0][0] == 1 and raw[0][1] == 1 and raw[0][2] == 1:
        win2 = True
    elif raw[1][0] == 1 and raw[1][1] == 1 and raw[1][2] == 1:
        win2 = True
    elif raw[2][0] == 1 and raw[2][1] == 1 and raw[2][2] == 1:
        win2 = True
    #  Diagonal wins
    elif raw[0][0] == 1 and raw[1][1] == 1 and raw[2][2] == 1:
        win2 = True
    elif raw[0][2] == 1 and raw[1][1] == 1 and raw[2][0] == 1:
        win2 = True
    else:
        win2 = False
    return win2


#  Turn raw board array into graphical representation
def print_board(raw):
    board = ""
    y_guide = 0
    board += '    0   1   2  \n'
    board += '  -------------\n'
    for row in raw:
        board += f'{y_guide} | '
        for item in row:
            if item == -1:
                alp_item = 'X'
            elif item == 0:
                alp_item = ' '
            elif item == 1:
                alp_item = 'O'
            board += f'{alp_item} | '
        board += '\n  -------------\n'
        y_guide += 1

    return board