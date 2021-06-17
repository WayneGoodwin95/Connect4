import pygame as pg
import numpy as np

import game_functions as gf

from game_objects import Settings
from game_objects import Tile
from game_objects import Game_over
from game_objects import Button


def run_game():
    # Initialise game, settings, and create screen object
    settings = Settings()
    pg.init()
    screen = pg.display.set_mode((settings.screen_width, settings.screen_height))
    pg.display.set_caption('Connect 4')

    # Create board, play button, and initialise game over screen
    board = gf.create_board(screen, settings, Tile)

    play_button = Button(screen, 'Play')
    game_over = Game_over(screen)

    # Draw the first screen
    screen.fill(settings.bg_color)
    gf.draw_board(board)
    gf.update_screen(screen, settings, board, play_button, game_over)

    # Start the main loop for game
    while True:
        # Check if event has occurred (player moved or clicked play button
        played, play_button_clicked = gf.check_event(settings, board, play_button)

        # Check if the player move results in a win and change player
        if settings.game_active and played:
            gf.check_win(settings, board, game_over)
            settings.change_player()
            # If the play is not a winning move. Update playable tiles
            if settings.game_active:
                gf.playable_tile(settings, board)

        # Update screen if player clicks on an event
        if played or play_button_clicked:
            gf.update_screen(screen, settings, board, play_button, game_over)


run_game()