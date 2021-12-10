import random

import numpy as np
import pygame
import math
from init import COLUMN_COUNT, ROW_COUNT

COLORBLUE = (0, 0, 255)
COLORBLACK = (0, 0, 0)
COLORRED = (255, 0, 0)
COLORYELLOW = (255, 255, 0)
COLORPINK = (255, 192, 203)

PLAYER1 = 1
PLAYER2 = 2
AI = 3

PLAYER1_PIECE = 1
PLAYER2_PIECE = 2
AI_PIECE = 3

LENGTH_WINDOW = 4
EMPTY = 0


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


# initializing the required variables for the screen
SQUARESIZE = 100
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE
size = (width, height)
RADIUS = int(SQUARESIZE / 2 - 4)
screen = pygame.display.set_mode(size)


# draw the actual animated board
def draw_board(board):
    # for empty spaces
    for iterator_column in range(COLUMN_COUNT):
        for iterator_row in range(ROW_COUNT):
            pygame.draw.rect(screen, COLORBLUE, (
                iterator_column * SQUARESIZE, iterator_row * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, COLORBLACK, (int(iterator_column * SQUARESIZE + SQUARESIZE / 2),
                                                    int(iterator_row * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)),
                               RADIUS)
    # for pieces(player1 and player2)
    for iterator_column in range(COLUMN_COUNT):
        for iterator_row in range(ROW_COUNT):
            if board[iterator_row][iterator_column] == PLAYER1_PIECE:
                pygame.draw.circle(screen, COLORRED, (int(iterator_column * SQUARESIZE + SQUARESIZE / 2),
                                                      height - int(iterator_row * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif board[iterator_row][iterator_column] == PLAYER2_PIECE:
                pygame.draw.circle(screen, COLORYELLOW, (int(iterator_column * SQUARESIZE + SQUARESIZE / 2),
                                                         height - int(iterator_row * SQUARESIZE + SQUARESIZE / 2)),
                                   RADIUS)
            elif board[iterator_row][iterator_column] == AI_PIECE:
                pygame.draw.circle(screen, COLORPINK, (int(iterator_column * SQUARESIZE + SQUARESIZE / 2),
                                                       height - int(iterator_row * SQUARESIZE + SQUARESIZE / 2)),
                                   RADIUS)
    pygame.display.update()


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


def score_possible_position(board, piece):
    output_score = 0
    # Score Horizontal
    for iterator_row in range(ROW_COUNT):
        row_array = [int(i) for i in list(board[iterator_row, :])]
        for iterator_column in range(COLUMN_COUNT - 3):
            window_horizontal = row_array[iterator_column:iterator_column + LENGTH_WINDOW]

            if window_horizontal.count(piece) == 4:
                output_score += 50
            elif window_horizontal.count(piece) == 3 and window_horizontal.count(EMPTY) == 1:
                output_score += 5

    # Score Vertical
    for iterator_column in range(COLUMN_COUNT):
        column_array = [int(i) for i in list(board[:, iterator_column])]
        for iterator_row in range(ROW_COUNT - 3):
            window_vertical = column_array[iterator_row:iterator_row + LENGTH_WINDOW]

            if window_vertical.count(piece) == 4:
                output_score += 50
            elif window_vertical.count(piece) == 3 and window_vertical.count(EMPTY) == 1:
                output_score += 5

    # Score right diag
    for iterator_row in range(ROW_COUNT - 3):
        for iterator_column in range(COLUMN_COUNT - 3):
            window_right_diag = [board[iterator_row + i][iterator_column + i] for i in range(LENGTH_WINDOW)]

            if window_right_diag.count(piece) == 4:
                output_score += 50
            elif window_right_diag.count(piece) == 3 and window_right_diag.count(EMPTY) == 1:
                output_score += 5

    # Score left diag
    for iterator_row in range(ROW_COUNT - 3):
        for iterator_column in range(COLUMN_COUNT - 3):
            window_left_diag = [board[iterator_row + 3 - i][iterator_column + i] for i in range(LENGTH_WINDOW)]

            if window_left_diag.count(piece) == 4:
                output_score += 50
            elif window_left_diag.count(piece) == 3 and window_left_diag.count(EMPTY) == 1:
                output_score += 5

    return output_score


def get_locations(board):
    valid_location_list = []
    for iterator_column in range(COLUMN_COUNT):
        if is_valid_location(board, iterator_column):
            valid_location_list.append(iterator_column)
    return valid_location_list


def put_best_move_possible(board, piece):
    best_score = 0
    my_valid_location_list = get_locations(board)
    best_column = random.choice(my_valid_location_list)
    for iterator_column in my_valid_location_list:
        aux_row = get_empty_row(board, iterator_column)
        temp = board.copy()
        put_piece(temp, aux_row, iterator_column, piece)
        score = score_possible_position(temp, piece)
        if score > best_score:
            best_score = score
            best_column = iterator_column

    return best_column
