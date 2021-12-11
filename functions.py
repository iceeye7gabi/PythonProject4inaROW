import random
import numpy as np
import math
from init import COLUMN_COUNT, ROW_COUNT
from variables import *


# initialize the matrix for the game
def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board


# place the piece into the board of the game
def put_piece(board, row, column, piece):
    board[row][column] = piece


# verify if you can place the piece in the spot
def is_valid_location(board, column):
    return board[ROW_COUNT - 1][column] == 0


# return the first empty(available) row
def get_empty_row(board, column):
    for iterator_row in range(ROW_COUNT):
        if board[iterator_row][column] == 0:
            return iterator_row


# print the board(we need to flip because of numpy)
def print_board(board):
    print(np.flip(board, 0))


# check if a player won after every move
def winning_conditions(board, piece):
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


# evaluate how many points each line gives
def evaluate(line, piece):
    enemy_piece = PLAYER1_PIECE
    if piece == PLAYER1_PIECE:
        enemy_piece = AI_PIECE

    score = 0
    if line.count(piece) == 4:
        score += POINT_BAR * 10
    elif line.count(piece) == 3 and line.count(EMPTY) == 1:
        score += POINT_BAR
    elif line.count(piece) == 2 and line.count(EMPTY) == 2:
        score += POINT_BAR//2

    if line.count(enemy_piece) == 3 and line.count(EMPTY) == 1:
        score -= POINT_BAR

    return score


# calculate the score depending on the situation
def score_possible_position(board, piece):
    output_score = 0

    # Score Horizontal
    for iterator_row in range(ROW_COUNT):
        row_array = [int(i) for i in list(board[iterator_row, :])]
        for iterator_column in range(COLUMN_COUNT - 3):
            line_horizontal = row_array[iterator_column:iterator_column + LENGTH_WINDOW]

            output_score += evaluate(line_horizontal, piece)

    # Score Vertical
    for iterator_column in range(COLUMN_COUNT):
        column_array = [int(i) for i in list(board[:, iterator_column])]
        for iterator_row in range(ROW_COUNT - 3):
            line_vertical = column_array[iterator_row:iterator_row + LENGTH_WINDOW]

            output_score += evaluate(line_vertical, piece)

    # Score right diag
    for iterator_row in range(ROW_COUNT - 3):
        for iterator_column in range(COLUMN_COUNT - 3):
            line_right_diag = [board[iterator_row + i][iterator_column + i] for i in range(LENGTH_WINDOW)]

            output_score += evaluate(line_right_diag, piece)

    # Score left diag
    for iterator_row in range(ROW_COUNT - 3):
        for iterator_column in range(COLUMN_COUNT - 3):
            line_left_diag = [board[iterator_row + 3 - i][iterator_column + i] for i in range(LENGTH_WINDOW)]

            output_score += evaluate(line_left_diag, piece)

    return output_score


# returns a list containing all valid locations
def get_locations(board):
    valid_location_list = []
    for iterator_column in range(COLUMN_COUNT):
        if is_valid_location(board, iterator_column):
            valid_location_list.append(iterator_column)
    return valid_location_list


# check if the game board is in a final state(someone won the game or no more available locations)
def is_final_state(board):
    return len(get_locations(board)) == 0 or winning_conditions(board, AI_PIECE) \
           or winning_conditions(board, PLAYER1_PIECE)


# minmax algorithm
def minmax_algorithm(board, depth, maximizing_player):
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
                new_generated_score = minmax_algorithm(aux_board, depth - 1, True)[0]
                if new_generated_score < val:
                    val = new_generated_score
                    best_column = iterator_column
            return val, best_column


# minmax algorithm with alpha_beta pruning
def minmax_algorithm_with_alpha_beta_pruning(board, depth, alpha, beta, maximizing_player):
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
