"""
EFREITRIS
Julien BOUDJEDID
Paul Leflon

Main functions for game functionalities/interactions.
"""
def main(stdscr):
    """
    This function is the main function of the game. It is called when the game is launched.
    :param stdscr: the screen
    :return: None
    """
    # we initialize the necessary values and variables
    color_setup()
    global score, board, saved
    board = None
    saved = False
    score = 0
    stdscr.clear()
    stdscr.refresh()
    # we create the gameboard
    display_menu(stdscr)
    boardintel = display_menu_options(stdscr)
    board_size, board_type, difficulty = boardintel[0], boardintel[1], boardintel[2]
    if boardintel == "RECOVER":
        saved = True
        board, score, boardsize, boardtype, difficulty = recoverfromfiles()
    else:
        board = deepcopy(globals()[f'{board_size}_{board_type}_BOARD'])
    x = True
    while x:  # we loop until the game is closed
        x = gameloop(stdscr, board_size, board_type, difficulty, saved)
        if saved:  # if the game is recovered, we don't want to loop
            saved = False
