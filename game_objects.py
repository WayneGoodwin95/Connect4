import pygame as pg


class Settings():
    def __init__(self):
        # Screen settings
        self.bg_color = (32, 44, 201)
        self.screen_height = 800
        self.screen_width = 914

        # Board settings
        self.cols = 7
        self.rows = 6

        # Game settings
        self.win_number = 4
        self.cur_player = 1
        self.game_active = False
        self.game_over_msg = ''

        # play settings
        self.current_row = 0
        self.current_col = 0

    def change_player(self):
        """ Change the player. """
        if self.cur_player == 1:
            self.cur_player = 2
        elif self.cur_player == 2:
            self.cur_player = 1

    def reset_settings(self):
        self.game_active = True
        self.game_over_msg = ''
        self.current_row = 0
        self.current_col = 0


class Tile(Settings):

    def __init__(self, screen, row, col):
        Settings.__init__(self)

        self.screen = screen
        self.row = row
        self.col = col

        # Tile counter dimensions
        self.radius = self.screen_height / 14
        self.diameter = self.radius * 2


        # Tile colors
        self.player1_color = (255, 0, 0)
        self.player2_color = (255, 255, 0)
        self.no_color = (255, 255, 255)
        self.color = (255, 255, 255)

        self.player = 0
        self.active = False

        # Create the tile positions for screen
        self.ypos = int((self.diameter * row) + (self.diameter * 0.5))
        self.xpos = int((self.diameter * col) + (self.diameter * 0.5))

        # Create the Rect (circle) and center it
        self.circle = pg.Rect(self.xpos, self.ypos, self.diameter, self.diameter)
        self.center = self.circle.center

        # Make tiles playable for the bottom row
        if row == 5:
            self.active = True

    def update_tile(self, player):
        self.active = False
        self.player = player
        if self.player == 1:
            self.color = self.player1_color
        elif self.player == 2:
            self.color = self.player2_color

    def reset_tile(self):
        self.player = 0
        self.color = self.no_color

        if self.row == 5:
            self.active = True
        else:
            self.active = False

    def draw_tile(self):
        pg.draw.circle(self.screen, self.color, self.center, self.radius, 0)


class Game_over(Settings):
    def __init__(self, screen):
        Settings.__init__(self)
        """Initialise button attributes."""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width = self.screen_width / 10
        self.height = self.screen_height / 10
        self.text_color = (255, 24, 24)
        self.bg_color = None
        self.font = pg.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.rect = pg.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.centery -= self.height

        # The button message needs to be prepped only once
        self.msg = " "
        self.prep_msg()

    def prep_msg(self):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(self.msg, True, self.text_color, self.bg_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_msg(self):
        # Draw blank button and then draw message.
        self.screen.blit(self.msg_image, self.msg_image_rect)


class Button(Game_over):
    def __init__(self, screen, msg):
        Game_over.__init__(self, screen)
        """Initialise button attributes."""
        # Change background color and text color for buttons
        self.bg_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.rect.centery += self.height

        self.msg = msg
        # The button message needs to be prepped only once
        self.prep_msg()

    def draw_button(self):
        # Draw blank button and then draw message.
        self.screen.fill(self.bg_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)