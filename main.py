import pygame as pg
import numpy as np

from settings import Settings
import game_functions as gf
from button import Button
from win_message import Game_over


def run_game():
    # Initialise game, settings, and create screen object
    settings = Settings()
    pg.init()
    screen = pg.display.set_mode((settings.screen_width, settings.screen_height))
    pg.display.set_caption('Connect 4')

    # Create board, play button, and initialise game over screen
    board = gf.create_board(settings)
    play_button = Button(screen, settings, 'Play')
    game_over_screen = Game_over(screen, settings)

    # Draw the first screen
    screen.fill(settings.bg_color)
    gf.draw_board(screen, settings, board)
    gf.update_screen(screen, settings, board, play_button, game_over_screen)

    # Start the main loop for game
    while True:
        # Check if event has occurred (player moved or clicked play button
        played, play_button_clicked = gf.check_event(settings, board, play_button)

        # Check if the player move results in a win and change player
        if settings.game_active and played:
            gf.check_win(settings, board)
            gf.change_player(settings)
            # If the play is not a winning move. Update playable tiles
            if settings.game_active:
                gf.playable_tile(settings, board)

        # Update screen if player clicks on an event
        if played or play_button_clicked:
            gf.update_screen(screen, settings, board, play_button, game_over_screen)


run_game()