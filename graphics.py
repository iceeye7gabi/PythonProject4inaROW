import pygame
import variables

from init import ROW_COUNT, COLUMN_COUNT
from variables import *

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
            pygame.draw.rect(screen, variables.COLORBLUE, (
                iterator_column * SQUARESIZE, iterator_row * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, variables.COLORBLACK, (int(iterator_column * SQUARESIZE + SQUARESIZE / 2),
                                                              int(iterator_row * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)),
                               RADIUS)
    # for pieces(player1 and player2)
    for iterator_column in range(COLUMN_COUNT):
        for iterator_row in range(ROW_COUNT):
            if board[iterator_row][iterator_column] == variables.PLAYER1_PIECE:
                pygame.draw.circle(screen, variables.COLORRED, (int(iterator_column * SQUARESIZE + SQUARESIZE / 2),
                                                                height - int(
                                                                    iterator_row * SQUARESIZE + SQUARESIZE / 2)),
                                   RADIUS)
            elif board[iterator_row][iterator_column] == variables.PLAYER2_PIECE:
                pygame.draw.circle(screen, variables.COLORYELLOW, (int(iterator_column * SQUARESIZE + SQUARESIZE / 2),
                                                                   height - int(
                                                                       iterator_row * SQUARESIZE + SQUARESIZE / 2)),
                                   RADIUS)
            elif board[iterator_row][iterator_column] == variables.AI_PIECE:
                pygame.draw.circle(screen, variables.COLORPINK, (int(iterator_column * SQUARESIZE + SQUARESIZE / 2),
                                                                 height - int(
                                                                     iterator_row * SQUARESIZE + SQUARESIZE / 2)),
                                   RADIUS)
    pygame.display.update()


# winning screen for AI
def show_ai_win_screen():
    font = pygame.font.SysFont("arial", int(height / 9))
    pygame.time.wait(500)
    pygame.draw.rect(screen, variables.COLORWHITE, (0, 0, width, height))
    label = font.render("AI WON!", True, variables.COLORPINK)
    screen.blit(label, (height / 4, 4 * width / 9))
    pygame.display.update()
    pygame.time.wait(3000)


# winning screen for Player1
def show_player1_win_screen():
    font = pygame.font.SysFont("arial", int(height / 9))
    pygame.time.wait(500)
    pygame.draw.rect(screen, variables.COLORRED, (0, 0, width, height))
    label = font.render("PLAYER1 WON!", True, variables.COLORPINK)
    screen.blit(label, (height / 4, 4 * width / 9))
    pygame.display.update()
    pygame.time.wait(3000)


# wining screen for Player2
def show_player2_win_screen():
    font = pygame.font.SysFont("arial", int(height / 9))
    pygame.time.wait(500)
    pygame.draw.rect(screen, variables.COLORYELLOW, (0, 0, width, height))
    label = font.render("PLAYER2 WON!", True, variables.COLORPINK)
    screen.blit(label, (height / 4, 4 * width / 9))
    pygame.display.update()
    pygame.time.wait(3000)


def show_ai_levels_screen():
    font = pygame.font.SysFont("arial", int(height / 7))

    # choose AI level screen
    pygame.draw.rect(screen, COLORWHITE, (0, 0, width, height))
    pygame.draw.rect(screen, COLORRED, (0, 2 * width / 3, width, height / 3))
    pygame.draw.rect(screen, COLORYELLOW, (0, width / 3, width, height / 3))
    pygame.draw.rect(screen, COLORWHITE, (0, 0, width, height / 3))

    label = font.render("EASY", True, COLORPINK)
    screen.blit(label, (height / 3, width / 9))

    label = font.render("MEDIUM", True, COLORPINK)
    screen.blit(label, (height / 4, 4 * width / 9))

    label = font.render("HARD", True, COLORPINK)
    screen.blit(label, (height / 3, 7 * width / 9))
