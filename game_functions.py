import sys

import pygame as pg
import numpy as np
import win_conditions as wc


def check_event(settings, board, play_button):
    """ Respond to keyboard and mouse presses"""
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()
            if settings.game_active:
                played = check_can_play(settings, board, mouse_pos)
                return played, False
            elif not settings.game_active:
                play_button_clicked = check_play_button(settings, board, mouse_pos, play_button)
                return False, play_button_clicked
    return False, False


def check_can_play(settings, board, mouse_pos):
    """ Check if the player can play the tile in position clicked"""
    for index, value in np.ndenumerate(board):
        row, col = index[0], index[1]
        if board[row][col].circle.collidepoint(mouse_pos) and board[row][col].active == True:
            player = settings.cur_player
            board[row][col].update_tile(player)
            settings.current_row = row
            settings.current_col = col
            return True
    return False


def check_play_button(settings, board, mouse_pos, play_button):
    """ Start a new game when the player clicks play. """
    if play_button.rect.collidepoint(mouse_pos):
        reset_board(board)
        settings.reset_settings()
        return True
    return False


def create_board(screen, settings, Tile):
    """ Create the board. """
    board = np.empty((settings.rows, settings.cols), dtype=object)
    for index, value in np.ndenumerate(board):
        row, col = index[0], index[1]
        # Create tile Dictionary in the board
        board[row][col] = Tile(screen, row, col)
    # Return the board
    return board


def playable_tile(settings, board):
    """ Update board playable tiles"""
    if settings.current_row > 0:
        board[settings.current_row - 1][settings.current_col].active = True


def check_win(settings, board, game_over):
    """ Check if player wins in each direction. """
    wc.check_horizontal(settings, board, game_over)
    wc.check_down(settings, board, game_over)
    wc.check_diagonal_nw_se(settings, board, game_over)
    wc.check_diagonal_ne_sw(settings, board, game_over)


def reset_board(board):
    """ Reset the board to original state"""
    for index, value in np.ndenumerate(board):
        row, col = index[0], index[1]
        board[row][col].reset_tile()


def draw_board(board):
    """ Draw the board. """
    for index, value in np.ndenumerate(board):
        row, col = index[0], index[1]
        board[row][col].draw_tile()


def update_screen(screen, settings, board, play_button, game_over):
    """ Update the screen. """

    # Fill the background color and draw the board over it
    screen.fill(settings.bg_color)
    draw_board(board)

    # if the game is not active. Draw the game over and play button
    if not settings.game_active:
        game_over.prep_msg()
        game_over.draw_msg()
        play_button.draw_button()

    # Update the display
    pg.display.update()
