import random
import numpy as np
import math
from init import COLUMN_COUNT, ROW_COUNT
from variables import *


def create_board():
    """
    initialize the matrix for the game using numpy.zeros

    :return: a matrix of 0 representing the board of the game
    """
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board


def put_piece(board, row, column, piece):
    """
    place the piece into the board of the game

    :param board: the matrix of the game
    :param row: the row where we put the piece
    :param column: the column where we put the piece
    :param piece: the piece which will be placed on the board
    :return:void
    """
    board[row][column] = piece


def is_valid_location(board, column):
    """
    verify if you can place the piece in the spot
    if the spot is empty, we can put the piece there

    :param board: the matrix of the game
    :param column: the column where we verify if we can put the piece there
    :return: true if we can put the piece there, else false, we cannot put the piece there
    """
    if board[ROW_COUNT - 1][column] == 0:
        return True
    else:
        return False


def get_empty_row(board, column):
    """
    return the first empty(available) row

    :param board: the matrix of the game
    :param column: the column where we verify if it's empty
    :return: the first row where we can put the piece
    """
    for iterator_row in range(ROW_COUNT):
        if board[iterator_row][column] == 0:
            return iterator_row


def print_board(board):
    """
    print the board(we need to flip because of numpy)

    :param board: matrix of the game
    :return: void
    """
    print(np.flip(board, 0))


def winning_conditions(board, piece):
    """
    check if a player won after every move
    we verify this in 4 ways: horizontally, vertically and both left and right diagonals

    :param board: the matrix of the game
    :param piece: the piece of the player which we verify
    :return: true if we have a 4inarow from a player else false
    """
    # check horizontally
    for iterator_column in range(COLUMN_COUNT - 3):
        for iterator_row in range(ROW_COUNT):
            if board[iterator_row][iterator_column] == piece and board[iterator_row][
                iterator_column + 1] == piece and board[iterator_row][iterator_column + 2] == piece and \
                    board[iterator_row][iterator_column + 3] == piece:
                return True

    # check vertically
    for iterator_column in range(COLUMN_COUNT):
        for iterator_row in range(ROW_COUNT - 3):
            if board[iterator_row][iterator_column] == piece and board[iterator_row + 1][
                iterator_column] == piece and board[iterator_row + 2][iterator_column] == piece and \
                    board[iterator_row + 3][iterator_column] == piece:
                return True

    # check right diag
    for iterator_column in range(COLUMN_COUNT - 3):
        for iterator_row in range(ROW_COUNT - 3):
            if board[iterator_row][iterator_column] == piece and board[iterator_row + 1][
                iterator_column + 1] == piece and board[iterator_row + 2][iterator_column + 2] == piece and \
                    board[iterator_row + 3][iterator_column + 3] == piece:
                return True

    # check left diag
    for iterator_column in range(COLUMN_COUNT - 3):
        for iterator_row in range(3, ROW_COUNT):
            if board[iterator_row][iterator_column] == piece and board[iterator_row - 1][
                iterator_column + 1] == piece and board[iterator_row - 2][iterator_column + 2] == piece and \
                    board[iterator_row - 3][iterator_column + 3] == piece:
                return True


def evaluate(line, piece):
    """
    Evaluate how many points each line gives
    I made a system where I use a point_bar which have a value
    So, in this case we have multiple scenarios: if we have 4inarow, it's obvious it should have the highest score
    And so on, for 3inarow and 2inarow
    Also, we do the same for the casual player, so AI can block the player when he could get a 4inarow(a win)

    :param line: which line/formation of pieces we verify
    :param piece: the piece of the player/AI
    :return: the score after evaluation of the situation in the game
    """
    enemy_piece = PLAYER1_PIECE
    if piece == PLAYER1_PIECE:
        enemy_piece = AI_PIECE

    score = 0
    if line.count(piece) == 4:
        score += POINT_BAR * 10
    elif line.count(piece) == 3 and line.count(NO_PIECE_PLACED) == 1:
        score += POINT_BAR
    elif line.count(piece) == 2 and line.count(NO_PIECE_PLACED) == 2:
        score += POINT_BAR//2

    if line.count(enemy_piece) == 3 and line.count(NO_PIECE_PLACED) == 1:
        score -= POINT_BAR
    elif line.count(enemy_piece) == 2 and line.count(NO_PIECE_PLACED) == 2:
        score -= POINT_BAR // 2 + 1

    return score


def score_possible_position(board, piece):
    """
    Calculate the score depending on the situation.
    We have 4 ways: horizontally, vertically and both left and right diagonals
    For the first 2 cases: for every row/column, we create the list which contains all elements of the matrix
    with the rule [iterator_row][iterator] or [iterator][iterator_column].
    In this case, we get all the combination we need to evaluate the score.
    Then, for every row/column we take the formation from the above list and we evaluate it, in order to find the score.

    For the diagonals, we start iterating with the rows from top with i = 0 to i = 4
    Then, for every formation we evaluate the score.

    :param board: the matrix of the game
    :param piece: the piece of the player
    :return: the score generated after scoring every possible move.
    """
    output_score = 0

    # Score Horizontal
    for iterator_row in range(ROW_COUNT):
        aux_arr_rows = list()
        for iterator in range(COLUMN_COUNT):
            aux_arr_rows.append(board[iterator_row, iterator])
        for iterator_column in range(COLUMN_COUNT - 3):
            horizontal_formation = aux_arr_rows[iterator_column:iterator_column + CONNECTED4_UNITS]
            output_score += evaluate(horizontal_formation, piece)

    # Score Vertical
    for iterator_column in range(COLUMN_COUNT):
        aux_arr_columns = list()
        for iterator in range(ROW_COUNT):
            aux_arr_columns.append(board[iterator, iterator_column])
        for iterator_row in range(ROW_COUNT - 3):
            vertical_formation = aux_arr_columns[iterator_row:iterator_row + CONNECTED4_UNITS]
            output_score += evaluate(vertical_formation, piece)

    # Score right diag
    for iterator_row in range(ROW_COUNT - 3):
        for iterator_column in range(COLUMN_COUNT - 3):
            right_diagonal_formation = [board[iterator_row + iterator][iterator_column + iterator] for iterator in range(CONNECTED4_UNITS)]
            output_score += evaluate(right_diagonal_formation, piece)

    # Score left diag
    for iterator_row in range(ROW_COUNT - 3):
        for iterator_column in range(COLUMN_COUNT - 3):
            left_diagonal_formation = [board[iterator_row + 3 - iterator][iterator_column + iterator] for iterator in range(CONNECTED4_UNITS)]
            output_score += evaluate(left_diagonal_formation, piece)

    return output_score


def get_locations(board):
    """
    returns a list containing all valid locations

    :param board: the matrix of the game
    :return: a list with all available locations to put a piece
    """
    valid_location_list = []
    for iterator_column in range(COLUMN_COUNT):
        if is_valid_location(board, iterator_column):
            valid_location_list.append(iterator_column)
    return valid_location_list


def is_final_state(board):
    """
    check if the game board is in a final state(someone won the game or no more available locations)

    :param board: the matrix of the gmae
    :return: true if at least one the three conditions are true: we don't have any available locations on the board
    or AI won the game OR the player won the game
    """
    return len(get_locations(board)) == 0 or winning_conditions(board, AI_PIECE) \
           or winning_conditions(board, PLAYER1_PIECE)


def minmax_algorithm(board, depth, maximizing_player):
    """
    minmax algorithm
    https://en.wikipedia.org/wiki/Minimax
    If depth == 0(leaf nodes of the tree) or someone won the game, we return a big value regarding who won.
    Else, we don't have any more moves, we close the game.
    Else, if depth is 0, we evaluate the score

    Else, for maximizing_player(AI), we take a very low value and a random column as our best column.
    Then, we iterate through every column in every location we can put a piece. We get the first open row we have
    We make a copy of the board so we dont alterate our initial board, we put the piece in the copy board
    And then we call the minmax again for the new_board, depth - 1 and minimizingPlayer.
    After, we check the score for every iteration and we get the higest score.(and the column who generated that score)

    If we are minimazing player  we call the minmax again for new_board, depth - 1 and maximizingPlayer
    We take the lowest value(instead of the higest from maximizingPlayer)

    :param board: the matrix of the game
    :param depth: the depth of the tree
    :param maximizing_player: AI
    :return: the higest score after all the iterations of the algorithm + the column
    """
    is_final = is_final_state(board)
    locations = get_locations(board)
    if depth == 0 or is_final:
        if is_final:
            if winning_conditions(board, PLAYER1_PIECE):
                return -math.inf, None
            elif winning_conditions(board, AI_PIECE):
                return math.inf, None
            else:  # No valid moves remaining
                return 0, None
        else:  # depth = 0
            return score_possible_position(board, AI_PIECE), None
    else:
        if maximizing_player:
            val = -math.inf
            best_column = random.choice(locations)
            for iterator_column in locations:
                aux_board = board.copy()
                my_row = get_empty_row(board, iterator_column)
                put_piece(aux_board, my_row, iterator_column, AI_PIECE)
                # new_generated_score = max(val, minmax_algorithm(aux_board, depth - 1, False))
                new_generated_score = minmax_algorithm(aux_board, depth - 1, False)[0]
                if new_generated_score > val:
                    val = new_generated_score
                    best_column = iterator_column
            return val, best_column
        else:  # Minimizing level
            val = math.inf
            best_column = random.choice(locations)
            for iterator_column in locations:
                aux_board = board.copy()
                my_row = get_empty_row(board, iterator_column)
                put_piece(aux_board, my_row, iterator_column, PLAYER1_PIECE)
                # new_generated_score = min(val, minmax_algorithm(aux_board, depth - 1, True))
                new_generated_score = minmax_algorithm(aux_board, depth - 1, True)[
                    0]
                if new_generated_score < val:
                    val = new_generated_score
                    best_column = iterator_column
            return val, best_column


def minmax_algorithm_with_alpha_beta_pruning(board, depth, alpha, beta, maximizing_player):
    """
    minmax algorithm
    https://en.wikipedia.org/wiki/Minimax
    https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
    If depth == 0(leaf nodes of the tree) or someone won the game, we return a big value regarding who won.
    Else, we don't have any more moves, we close the game.
    Else, if depth is 0, we evaluate the score

    Else, for maximizing_player(AI), we take a very low value and a random column as our best column.
    Then, we iterate through every column in every location we can put a piece. We get the first open row we have
    We make a copy of the board so we dont alterate our initial board, we put the piece in the copy board
    And then we call the minmax again for the new_board, depth - 1 and minimizingPlayer.
    After, we check the score for every iteration and we get the higest score.(and the column who generated that score)

    If we are minimazing player  we call the minmax again for new_board, depth - 1 and maximizingPlayer
    We take the lowest value(instead of the higest from maximizingPlayer) + the column

    Despite the classical minmax, we can go to deeper depths without sacrificing a lot of time by eliminating
    other moves we dont need to look into.
    When we evaluate the best score, we also evaluate alpha.
    If alpha >= beta, we break out of the loop.
    The same applies for beta, but the signs changes.

    :param board: the matrix of the game
    :param depth: the depth of the tree
    :param alpha:
    :param beta:
    :param maximizing_player: AI
    :return: the higest score after all the iterations of the algorithm + the column
    """
    is_final = is_final_state(board)
    locations = get_locations(board)
    if depth == 0 or is_final:
        if is_final:
            if winning_conditions(board, PLAYER1_PIECE):
                return -math.inf, None
            elif winning_conditions(board, AI_PIECE):
                return math.inf, None
            else:  # No valid moves remaining
                return 0, None
        else:  # depth = 0
            return score_possible_position(board, AI_PIECE), None
    else:
        if maximizing_player:
            val = -math.inf
            best_column = random.choice(locations)
            for iterator_column in locations:
                aux_board = board.copy()
                my_row = get_empty_row(board, iterator_column)
                put_piece(aux_board, my_row, iterator_column, AI_PIECE)
                # new_generated_score = max(val, minmax_algorithm(aux_board, depth - 1, False))
                new_generated_score = \
                    minmax_algorithm_with_alpha_beta_pruning(aux_board, depth - 1, alpha, beta, False)[0]
                if new_generated_score > val:
                    val = new_generated_score
                    best_column = iterator_column
                alpha = max(alpha, val)
                if alpha >= beta:
                    break
            return val, best_column
        else:  # Minimizing level
            val = math.inf
            best_column = random.choice(locations)
            for iterator_column in locations:
                aux_board = board.copy()
                my_row = get_empty_row(board, iterator_column)
                put_piece(aux_board, my_row, iterator_column, PLAYER1_PIECE)
                # new_generated_score = min(val, minmax_algorithm(aux_board, depth - 1, True))
                new_generated_score = minmax_algorithm_with_alpha_beta_pruning(aux_board, depth - 1, alpha, beta, True)[
                    0]
                if new_generated_score < val:
                    val = new_generated_score
                    best_column = iterator_column
                beta = min(beta, val)
                if beta <= alpha:
                    break
            return val, best_column
