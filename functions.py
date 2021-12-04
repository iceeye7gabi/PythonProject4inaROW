import numpy as np
import pygame
import sys
import math

ROW_COUNT = 6
COLUMN_COUNT = 7

COLORBLUE = (0, 0, 255)
COLORBLACK = (0, 0, 0)
COLORRED = (255, 0, 0)
COLORYELLOW = (255, 255, 0)


# initialize the matrix for the game
def create_board():
    board = np.zeros((6, 7))
    return board


# place the piece into the board of the game
def put_piece(board, row, column, piece):
    board[row][column] = piece


# verify if you can place the piece in the spot
def is_valid_location(board, column):
    return board[5][column] == 0


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
            if board[iterator_row][iterator_column] == 1:
                pygame.draw.circle(screen, COLORRED, (int(iterator_column * SQUARESIZE + SQUARESIZE / 2),
                                                      height - int(iterator_row * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif board[iterator_row][iterator_column] == 2:
                pygame.draw.circle(screen, COLORYELLOW, (int(iterator_column * SQUARESIZE + SQUARESIZE / 2),
                                                         height - int(iterator_row * SQUARESIZE + SQUARESIZE / 2)),
                                   RADIUS)
    pygame.display.update()
