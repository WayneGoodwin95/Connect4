class Settings():
    def __init__(self):
        # Screen settings
        self.bg_color = (32, 44, 201)
        self.screen_height = 800
        self.screen_width = 1000

        # Board settings
        self.cols = 7
        self.rows = 6

        # Tile settings
        self.player1_color = (255, 0, 0)
        self.player2_color = (255, 255, 0)
        self.tile_radius = self.screen_height / 14
        self.tile_color = (255, 255, 255)
        self.tile_height = self.tile_radius * 2
        self.tile_width = self.tile_radius * 2

        # Game settings
        self.win_number = 4
        self.player = 1
        self.game_active = False
        self.game_over_msg = ''

        # play settings
        self.current_row = 0
        self.current_col = 0
