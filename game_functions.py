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
    #TODO: simplify code by using lambda functions???
    for row in range(settings.rows):
        for col in range(settings.cols):
            if board[row][col]['tile_circle'].collidepoint(mouse_pos) and board[row][col]['tile_active'] == True:
                update_board(settings, board, row, col)
                settings.current_row = row
                settings.current_col = col
                return True
    return False


def check_play_button(settings, board, mouse_pos, play_button):
    """ Start a new game when the player clicks play. """
    if play_button.rect.collidepoint(mouse_pos):
        reset_board(settings, board)
        reset_settings(settings)
        return True
    return False


def create_board(settings):
    """ Create the board. """
    board = np.empty((settings.rows, settings.cols), dtype=dict)
    # TODO: simplify code by using lambda functions???
    for col in range(0, settings.cols):
        tile_active = False
        for row in range(0, settings.rows):
            # Create the tile positions for screen
            tile_ypos = int(settings.tile_height * row)
            tile_xpos = int(settings.tile_width * col)

            # Create the Rect and for the tile
            tile_circle = pg.Rect(tile_xpos, tile_ypos, settings.tile_height, settings.tile_width)
            tile_center = tile_circle.center

            # Make tiles playable for the bottom row
            if row == 5:
                tile_active = True

            # Create tile Dictionary in the board
            board[row][col] = {'tile_radius': settings.tile_radius, 'tile_center': tile_center,
                               'tile_color': settings.tile_color, 'player': 0, 'tile_active':
                                   tile_active, 'tile_circle': tile_circle}

    # Return the board
    return board


def update_board(settings, board, row, col):
    """ Update the board with the newly placed tile. """
    board[row][col]['player'] = settings.player

    # Make tile unplayable
    board[row][col]['tile_active'] = False

    # Update tile color depending on which player played
    if settings.player == 1:
        board[row][col]['tile_color'] = settings.player1_color
    elif settings.player == 2:
        board[row][col]['tile_color'] = settings.player2_color


def change_player(settings):
    """ Change the player. """
    if settings.player == 1:
        settings.player = 2
    elif settings.player == 2:
        settings.player = 1


def playable_tile(settings, board):
    """ Update board playable tiles"""
    if settings.current_row > 0:
        board[settings.current_row - 1][settings.current_col]['tile_active'] = True


def check_win(settings, board):
    """ Check if player wins in each direction. """
    wc.check_horizontal(settings, board)
    wc.check_down(settings, board)
    wc.check_diagonal_nw_se(settings, board)
    wc.check_diagonal_ne_sw(settings, board)


def reset_board(settings, board):
    """ Reset the board to original state"""
    # TODO: simplify code by using lambda functions???
    for row in range(settings.rows):
        for col in range(settings.cols):
            board[row][col]['player'] = 0
            board[row][col]['tile_color'] = settings.tile_color

            if row == 5:
                board[row][col]['tile_active'] = True
            else:
                board[row][col]['tile_active'] = False


def reset_settings(settings):
    """ Reset settings to original state. Except making the winning player go second. """
    settings.game_active = True
    settings.game_over_msg = ''
    settings.current_row = 0
    settings.current_col = 0


def draw_board(screen, settings, board):
    """ Draw the board. """
    # TODO: simplify code by using lambda functions???
    for col in range(0, settings.cols):
        for row in range(0, settings.rows):
            pg.draw.circle(screen, board[row][col]['tile_color'], board[row][col]['tile_center'], board[row][col]['tile_radius'], 0)


def update_screen(screen, settings, board, play_button, game_over_screen):
    """ Update the screen. """

    # Fill the background color and draw the board over it
    screen.fill(settings.bg_color)
    draw_board(screen, settings, board)

    # if the game is not active. Draw the game over and play button
    if not settings.game_active:
        game_over_screen.msg = settings.game_over_msg
        game_over_screen.prep_msg()
        game_over_screen.draw_game_over_screen()
        play_button.draw_button()

    # Update the display
    pg.display.update()
