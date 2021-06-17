def check_down(settings, board, game_over):
    """Check if the player wins in downward direction"""

    # Create a copy of the row and col the player placed
    row = settings.current_row
    col = settings.current_col

    # Check how many tiles the player has in a row, going down
    for win_counter in range(1, settings.win_number + 1):
        # Add 1 to column to check the next tile
        row += 1

        # Check if the number of counters in a row are less than number to win,
        # check if the column is not at the end of of board,
        # check if the player in tile is the same as the player who played.
        if win_counter < settings.win_number and row < settings.rows and board[row][col].player == settings.cur_player:
            win_counter += 1
        # if the player wins. End the game
        elif win_counter == settings.win_number:
            end_game(settings, game_over)
        else:
            break


def check_horizontal(settings, board, game_over):
    """Check tiles left and right to see if the player wins in horizontal direction"""
    left = check_left(settings, board)
    right = check_right(settings, board)

    # Check if the number of players tiles in a row are a win
    horizontal = left + right + 1
    if horizontal >= settings.win_number:
        end_game(settings, game_over)


def check_right(settings, board):
    # Create a copy of the row and col the player placed
    row = settings.current_row
    col = settings.current_col
    result = 0

    # Check how many tiles the player has in a row to the right
    for win_counter in range(1, settings.win_number):
        # Add 1 to column to check the next tile
        col += 1
        # Check if the number of counters in a row are less than number to win,
        # check if the column is not at the end of of board,
        # check if the player is in tile is the same as the player who played.
        if win_counter < settings.win_number and col < settings.cols and board[row][col].player == settings.cur_player:
            result += 1
        # if the player wins break loop and return result
        elif win_counter == settings.win_number:
            break
        # if the tile is not the same as the played tile. Break loop and return result
        else:
            break

    # Return the number of tiles in a row to the right
    return result


def check_left(settings, board):
    row = settings.current_row
    col = settings.current_col
    result = 0
    for win_counter in range(1, settings.win_number):
        col -= 1
        if win_counter < settings.win_number and col > 0 and board[row][col].player == settings.cur_player:
            result += 1
        elif win_counter == settings.win_number:
            break
        else:
            break

    return result


def check_diagonal_nw_se(settings, board, game_over):
    """Check tiles North West and South East to see if the player wins in the diagonal direction"""
    nw = check_nw(settings, board)
    se = check_se(settings, board)

    nw_se = nw + se + 1

    if nw_se >= settings.win_number:
        end_game(settings, game_over)


def check_nw(settings, board):
    row = settings.current_row
    col = settings.current_col
    result = 0
    for win_counter in range(1, settings.win_number):
        col -= 1
        row -= 1
        if win_counter < settings.win_number and row > 0 and col > 0 \
                and board[row][col].player == settings.cur_player:
            result += 1
        elif win_counter == settings.win_number:
            break
        else:
            break

    return result


def check_se(settings, board):
    row = settings.current_row
    col = settings.current_col
    result = 0
    for win_counter in range(1, settings.win_number):
        col += 1
        row += 1
        if win_counter < settings.win_number and row < settings.rows and col < settings.cols \
                and board[row][col].player == settings.cur_player:
            result += 1
        elif win_counter == settings.win_number:
            break
        else:
            break

    return result


def check_diagonal_ne_sw(settings, board, game_over):
    """Check tiles North East and South West to see if the player wins in the diagonal direction"""
    ne = check_ne(settings, board)
    sw = check_sw(settings, board)

    ne_sw = ne + sw + 1

    if ne_sw >= settings.win_number:
        end_game(settings, game_over)


def check_sw(settings, board):
    row = settings.current_row
    col = settings.current_col
    result = 0
    for win_counter in range(1, settings.win_number):
        row += 1
        col -= 1
        if win_counter < settings.win_number and row < settings.rows and col > 0 \
                and board[row][col].player == settings.cur_player:
            result += 1
        elif win_counter == settings.win_number:
            break
        else:
            break

    return result


def check_ne(settings, board):
    row = settings.current_row
    col = settings.current_col
    result = 0
    for win_counter in range(1, settings.win_number):
        row -= 1
        col += 1
        if win_counter < settings.win_number and row > 0 and col < settings.cols \
                and board[row][col].player == settings.cur_player:
            result += 1
        elif win_counter == settings.win_number:
            break
        else:
            break

    return result


def end_game(settings, game_over):
    """ Stop game running and update the players winning message"""
    settings.game_active = False
    game_over.msg = 'Player ' + str(settings.cur_player) + ' WINS'