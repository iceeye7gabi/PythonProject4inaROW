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


def draw_board(board):
    """
    draw the actual animated board
    here we generate in the first phase all the empty spaces(the board without any pieces in it)
    then we generate the pieces for every player, which will be over the black circles from above.
    this will be called everytime a new move is mode, so the board is refreshed everytime

    :param board:  the matrix of the game
    :return: void
    """
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


def show_ai_win_screen():
    """
    winning screen for AI
    a new graphic window where a message appears: AI WON!

    :return:void
    """
    font = pygame.font.SysFont("arial", int(height / 9))
    pygame.time.wait(500)
    pygame.draw.rect(screen, variables.COLORWHITE, (0, 0, width, height))
    label = font.render("AI WON!", True, variables.COLORPINK)
    screen.blit(label, (height / 4, 4 * width / 9))
    pygame.display.update()
    pygame.time.wait(3000)


def show_player1_win_screen():
    """
       winning screen for Player1
       a new graphic window where a message appears: Player1 WON!

       :return:void
       """
    font = pygame.font.SysFont("arial", int(height / 9))
    pygame.time.wait(500)
    pygame.draw.rect(screen, variables.COLORRED, (0, 0, width, height))
    label = font.render("PLAYER1 WON!", True, variables.COLORPINK)
    screen.blit(label, (height / 4, 4 * width / 9))
    pygame.display.update()
    pygame.time.wait(3000)


def show_player2_win_screen():
    """
       winning screen for Player2
       a new graphic window where a message appears: Player2 WON!

       :return:void
       """
    font = pygame.font.SysFont("arial", int(height / 9))
    pygame.time.wait(500)
    pygame.draw.rect(screen, variables.COLORYELLOW, (0, 0, width, height))
    label = font.render("PLAYER2 WON!", True, variables.COLORPINK)
    screen.blit(label, (height / 4, 4 * width / 9))
    pygame.display.update()
    pygame.time.wait(3000)


def show_ai_levels_screen():
    """
    choose AI difficulty screen
    we divide a window in 3 parts: easy medium and hard depending on the difficulty of the AI

    :return:void
    """
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


def show_player_turn(player):
    font = pygame.font.SysFont("arial", int(height / 9))
    if player == PLAYER1:
        label = font.render("Player1 turn", True, COLORPINK)
        screen.blit(label, (height / 3 + 130, width / 9 - 100))
    if player == PLAYER2:
        label = font.render("Player2 turn", True, COLORPINK)
        screen.blit(label, (height / 3 + 130, width / 9 - 100))
