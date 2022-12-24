"""
EFREITRIS
Julien BOUDJEDID
Paul Leflon

The main file, used to launch the game
"""
import json
import random
from copy import deepcopy
import os
import time
from constants.blocks import *
from constants.boards import *
from internal.game import *
from internal.mechanics import *
import curses

os.system('mode con: cols=70 lines=60')
# global usage vars
board_size = ""
board_type = ""
difficulty = ""
azerty = "azertyuiopqsdfghjklmwxcvbn"
score = 0


def write_data(board, score, board_size, board_type, difficulty):
    try:
        data = {
            'board': board,
            'score': score,
            'board_size': board_size,
            'board_type': board_type,
            'difficulty': difficulty
        }

        with open('data/data.savestate', 'w') as f:
            json.dump(data, f)
    except:
        pass


def recover_data():
    with open('data/data.savestate', 'r') as f:
        data = json.load(f)

    board = list(data['board'])
    score = int(data['score'])
    board_size = data['board_size']
    board_type = data['board_type']
    difficulty = data['difficulty']
    return board, score, board_size, board_type, difficulty


def display_menu(stdscr: curses.wrapper, x: int = 0) -> None:
    """"
    Displays the menu
    :param stdscr: the screen
    :param x: the x position of the menu
    :return: None
    """
    global score
    # Create a new pad (off-screen window)
    menu = curses.newpad(10, 65)
    try:
        # Add the menu text to the pad
        menu.addstr(0, x, '███████╗███████╗██████╗ ███████╗██╗████████╗██████╗ ██╗███████╗\n', curses.color_pair(1))
        menu.addstr(1, x, '██╔════╝██╔════╝██╔══██╗██╔════╝██║╚══██╔══╝██╔══██╗██║██╔════╝\n', curses.color_pair(2))
        menu.addstr(2, x, '█████╗  █████╗  ██████╔╝█████╗  ██║   ██║   ██████╔╝██║███████╗\n', curses.color_pair(3))
        menu.addstr(3, x, '██╔══╝  ██╔══╝  ██╔══██╗██╔══╝  ██║   ██║   ██╔══██╗██║╚════██║\n', curses.color_pair(4))
        menu.addstr(4, x, '███████╗██║     ██║  ██║███████╗██║   ██║   ██║  ██║██║███████║\n', curses.color_pair(5))
        menu.addstr(5, x, '╚══════╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚══════╝\n', curses.color_pair(6))
    except curses.error:
        pass
    # Display the pad
    menu.noutrefresh(0, 0, 0, 0, 10, 65)
    # Update the screen
    curses.doupdate()


def color_setup():
    """"
    Setup the color combinations to use for the terminal
    :return: None
    """
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_BLACK)


def display_menu_options(stdscr, x=0, y=0) -> tuple:
    """
    Displays the menu options
    :param stdscr:
    :param x:
    :param y:
    :return:
    """

    def main_menu(stdscr, x, y):
        questions.addstr(y, x, 'type in your choice using the corresponding key\n')
        questions.addstr(y + 1, x, 'A) Start Game\n')
        questions.addstr(y + 2, x, 'Z) Instructions\n')
        questions.addstr(y + 3, x, 'E) Recover save\n')
        questions.addstr(y + 4, x, 'R) Exit\n')
        questions.noutrefresh(0, 0, 10, 0, 40, 60)
        curses.doupdate()
        # get the player choice and do the corresponding action
        choice = stdscr.getkey()
        return choice

    def board_size_menu(stdscr, x, y):
        questions.addstr(y, x, 'Choose a board size:\n')
        questions.addstr(y + 1, x, 'A) SMALL')
        questions.addstr(y + 2, x, 'Z) MEDIUM')
        questions.addstr(y + 3, x, 'E) LARGE')
        questions.addstr(y + 4, x, 'R) return')
        questions.noutrefresh(0, 0, 10, 0, 40, 60)
        curses.doupdate()
        choice = stdscr.getkey()
        return choice

    def board_type_menu(stdscr, x, y):
        questions.addstr(y, x, 'Choose a board type:\n')
        questions.addstr(y + 1, x, 'A) CIRCLE')
        questions.addstr(y + 2, x, 'Z) DIAMOND')
        questions.addstr(y + 3, x, 'E) TRIANGULAR')
        questions.addstr(y + 4, x, 'R) return')
        questions.noutrefresh(0, 0, 10, 0, 40, 60)
        curses.doupdate()
        choice = stdscr.getkey()
        return choice

    def difficulty_menu(stdscr, x, y):
        questions.addstr(y, x, 'Choose a difficulty:\n')
        questions.addstr(y + 1, x, 'A) EASY')
        questions.addstr(y + 2, x, 'Z) MEDIUM')
        questions.addstr(y + 3, x, 'E) HARD')
        questions.addstr(y + 4, x, 'R) return')
        questions.noutrefresh(0, 0, 10, 0, 40, 60)
        curses.doupdate()
        choice = stdscr.getkey()
        return choice

    def invalid_input():
        questions.addstr(y + 5, x, 'invalid choice, try again\n')
        questions.noutrefresh(0, 0, 10, 0, 40, 60)
        curses.doupdate()
        time.sleep(1)
        questions.clear()

    global board_type, board_size, difficulty
    questions = curses.newpad(20, 60)
    inmenu = True
    # create a menu loop to interact through the menu levels
    while inmenu:
        choice = main_menu(stdscr, x, y)
        questions.noutrefresh(0, 0, 10, 0, 20, 60)
        curses.doupdate()
        if choice == 'a':  # we gather the info to start the game
            questions.clear()
            # get board size
            choice = board_size_menu(stdscr, x, y)
            if choice == 'a':
                board_size = "SMALL"
            elif choice == 'z':
                board_size = "MEDIUM"
            elif choice == 'e':
                board_size = "LARGE"
            elif choice == 'r':
                questions.clear()
                continue
            else:
                # we catch the invalid input and display a message
                invalid_input()
                continue
            # get board type
            questions.clear()
            choice = board_type_menu(stdscr, x, y)
            if choice == 'a':
                board_type = "CIRCLE"
            elif choice == 'z':
                board_type = "DIAMOND"
            elif choice == 'e':
                board_type = "TRIANGLE"
            elif choice == 'r':
                questions.clear()
                continue
            else:
                # we catch the invalid input and display a message
                invalid_input()
                continue
            # get difficulty
            questions.clear()
            choice = difficulty_menu(stdscr, x, y)
            if choice == 'a':
                difficulty = "EASY"
            elif choice == 'z':
                difficulty = "MEDIUM"
            elif choice == 'e':
                difficulty = "HARD"
            elif choice == 'r':
                questions.clear()
                continue
            else:
                # we catch the invalid input and display a message
                invalid_input()
                continue
            questions.clear()
            questions.noutrefresh(0, 0, 10, 0, 20, 60)
            curses.doupdate()
            return board_size, board_type, difficulty

        elif choice == 'z':
            # we display the instructions
            questions.addstr(y, x, "╔══════════════════════════════════════════════════════════════════╗")
            questions.addstr(y + 1, x, "║   Efreitris is a Tetris-like game. Your job is to fill a board   ║")
            questions.addstr(y + 2, x, "║  with blocks to clear lines and columns and earn the most points ║")
            questions.addstr(y + 3, x, "║   that you can! But place your blocks wisely.. If you fill the   ║")
            questions.addstr(y + 4, x, "║      board so much that you cannot place anymore, you lose.      ║")
            questions.addstr(y + 5, x, "╚══════════════════════════════════════════════════════════════════╝")
            questions.addstr(y + 6, x, "press anywhere to return to the menu")
            questions.noutrefresh(0, 0, 20, 0, 20, 62)
            curses.doupdate()
            choice = stdscr.getkey()
            questions.clear()
            continue
        elif choice == 'e':
            return "R"
        elif choice == 'r':
            exit()
        else:
            # we catch the invalid input and display a message
            invalid_input()
            continue


def gameloop(stdscr, board_size, board_type, difficulty, saved=False):
    """
    This function is the main game loop. It is called when the player starts a new game.
    :param stdscr: the screen
    :param board_size: chosen board size
    :param board_type: chosen board type
    :param difficulty: chosen difficulty
    :param saved: wether or not we are recovering a saved state
    :return: returns True if the game isn't over, False otherwise
    """
    # we initialize the blocks and recover the board if necessary
    global board, score

    def refresh_internal(gameboard):
        """
        This function refreshes the internal board
        """
        gameboard.noutrefresh(0, 0, 10, 0, 50, 60)
        curses.doupdate()

    def build_board(gameboard, width, height, board):
        """
        This function builds the board
        :param gameboard:
        :param width:
        :param height:
        :param board:
        :return: None
        """
        for i in range(width):
            gameboard.addstr(0, i * 2 + 4, chr(97 + i))
        for i in range(width * 2 + 4):
            gameboard.addstr(1, i, "═")
        for i in range(height):
            gameboard.addstr((i + 2), 0, chr(97 + i))
        for i in range(height + 2):
            gameboard.addstr(i + 1, 1, "║")
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 0:
                    gameboard.addstr(i + 2, (j + 2) * 2, " ")
                elif board[i][j] == 1:
                    gameboard.addstr(i + 2, (j + 2) * 2, "□")
                else:
                    gameboard.addstr(i + 2, (j + 2) * 2, "█", curses.color_pair(board[i][j] - 1))
        refresh_internal(gameboard)

    def available_blocs(board_type):
        """
        This function returns the available blocks for the chosen board type
        :param board_type:
        :return: block list
        """
        if board_type == "CIRCLE":
            return CIRCLE_BLOCKS
        elif board_type == "DIAMOND":
            return DIAMOND_BLOCKS
        elif board_type == "TRIANGLE":
            return TRIANGLE_BLOCKS

    def get_random_blocs(blocs):
        """
        This function returns a random block from the list of available blocks
        :param blocs:
        :return:
        """
        if difficulty == "MEDIUM":
            return [random.choice(blocks) for _ in range(3)]
        elif difficulty == "HARD":
            return [random.choice(blocks) for _ in range(2)]
        else:
            return [random.choice(blocks) for _ in range(5)]

    def display_bloc(gameboard, bloc, x, y, color, height):
        """

        :param gameboard:
        :param bloc:
        :param x:
        :param y:
        :param color:
        :param height:
        :return: None
        """
        for i in range(len(bloc)):
            for j in range(len(bloc[i])):
                if bloc[i][j] == 1:
                    gameboard.addstr(height + y + i + 2, x + j * 2, "■", curses.color_pair(color))

    def display_blocs(gameboard, available_blocs, colorlist, x, y, height):
        """
        This function displays the blocks, using the function display_bloc
        :param gameboard:
        :param available_blocs:
        :param colorlist:
        :param x:
        :param y:
        :param height:
        :return:
        """
        for i in range(len(available_blocks)):  # we display the blocks
            color = random.randint(1, 7)
            display_bloc(gameboard, available_blocks[i], x, 5, color, height)
            colorlist.append(color)
            gameboard.addstr(height + y + 8, x, f"block {azerty[i]}")
            x += 12
        refresh_internal(gameboard)
        return colorlist

    def choose_block(gameboard, available_blocs, board, score, board_size, board_type, difficulty):
        """
        This function allows the player to choose a block
        :param gameboard:
        :param available_blocs:
        :param board:
        :param score:
        :param board_size:
        :param board_type:
        :param difficulty:
        :return: the chosen block
        """
        tries = 0
        choice = stdscr.getkey()
        while choice not in azerty[:len(available_blocks):]:
            if choice == '&':  # we save the game
                write_data(board, score, board_size, board_type, difficulty)
                board = None
                return False  # we return False to indicate that the game is closed
            tries += 1
            gameboard.addstr(height + y + 10, 0, f"invalid choice, try again ({tries}/3)", curses.color_pair(1))
            refresh_internal(gameboard)
            if tries == 3:  # we return to the menu if the user has tried 3 times
                return False
            choice = stdscr.getkey()
        return choice

    def calculate_score(board, score):
        """
        This function calculates the score
        :param board:
        :param score:
        :return: additional score
        """
        score += block_value(block)
        col_score = 0
        cleared_cols_count = 0
        row_score = 0
        cleared_rows_count = 0
        for i in range(len(board)):
            if row_state(board, i):
                row_score += clear_row(board, i) * 3
                cleared_rows_count += 1
        for j in range(len(board[0])):
            if col_state(board, j):
                col_score += clear_col(board, j) * 3
                cleared_cols_count += 1
        total = col_score * cleared_cols_count + row_score + cleared_rows_count
        if cleared_cols_count != 0 and cleared_rows_count != 0:
            total *= min(cleared_cols_count, cleared_rows_count) * 2
        return total

    def select_position(gameboard, x, y, height):
        """
        This function allows the player to select a position
        :param gameboard:
        :param x:
        :param y:
        :param height:
        :return: the coordinates of the selected position
        """
        gameboard.addstr(height + y + 1, 0, f"you selected block {choice}", curses.color_pair(2))
        gameboard.addstr(height + y + 2, 0, "type in the x coordinate of the block", curses.color_pair(3))
        refresh_internal(gameboard)
        x_coord = stdscr.getkey()
        gameboard.addstr(height + y + 2, 0, "type in the y coordinate of the block", curses.color_pair(3))
        refresh_internal(gameboard)
        y_coord = stdscr.getkey()
        x_coord = ord(x_coord) - 97
        y_coord = ord(y_coord) - 97
        return x_coord, y_coord

    blocks = COMMON_BLOCKS.copy()
    blocks += available_blocs(board_type)
    if saved:
        board, score = recover_data()[:2]
    gameboard = curses.newpad(90, 60)
    gameboard.addstr(8, 50, f'score: {score}', curses.color_pair(1))
    gameboard.addstr(9, 50, f'{difficulty}', curses.color_pair(1))
    # we physically build the board on the screen
    width, height = actual_size(board)
    build_board(gameboard, width, height, board)
    # game loop for placing a block (or leaving)
    # we get the next blocks to display
    available_blocks = get_random_blocs(blocks)
    x = 0
    y = 5
    refresh_internal(gameboard)
    gameboard.addstr(height + y, 0,
                     f"select block with letter or '&' to save")
    y += 1
    gameboard.addstr(height + y, 0, "═" * (len(available_blocks) * 12))
    for i in range(1, 13):  # we clear the area where the blocks will be displayed
        gameboard.move(height + y + i, 0)
        gameboard.clrtoeol()
    colorlist = display_blocs(gameboard, available_blocks, [], x, y, height)
    # now that the blocks are displayed we need to prompt the user for a choice
    choice = choose_block(gameboard, available_blocks, board, score, board_size, board_type, difficulty)
    if type(choice) == bool:
        return False
    block = available_blocks[azerty.index(choice)]
    color = colorlist[azerty.index(choice)]
    selectpos = False
    tries = 0
    # now we need to select a position on the board
    while tries < 3:
        for i in range(1, 13):  # we clear the area where the blocks will be displayed
            gameboard.move(height + y + i, 0)
            gameboard.clrtoeol()
        # draw block again to show it's selected
        x, y = 0, 6
        display_bloc(gameboard, block, x, y, color, height)
        y += 6
        # we display the instructions
        x_coord, y_coord = select_position(gameboard, x, y, height)
        # we check if the block can be placed
        if valid_position(board, block, x_coord, y_coord):
            # we place the block
            place_block(board, block, x_coord, y_coord, color+1)
            # calculate score
            score = 0
            calculate_score(board, score)
            refresh_internal(gameboard)
            # we return true as the game isn't closed
            return True
        else:
            # we display an error message if the coordinates are invalid
            tries += 1
            gameboard.addstr(height + y + 3, 0, f"invalid position, try again ({tries}/3)", curses.color_pair(1))
            refresh_internal(gameboard)
    return False


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
    if type(boardintel) != str:
        board_size, board_type, difficulty = boardintel[0], boardintel[1], boardintel[2]
        board = deepcopy(globals()[f'{board_size}_{board_type}_BOARD'])
    else:
        saved = True
        board_size, board_type, difficulty = recover_data()[2:]
    x = True
    while x:  # we loop until the game is closed
        x = gameloop(stdscr, board_size, board_type, difficulty, saved)
        if saved:  # if the game is recovered, we don't want to loop
            saved = False


while True:  # we loop until we choose to quit the game in the menu
    curses.wrapper(main)
