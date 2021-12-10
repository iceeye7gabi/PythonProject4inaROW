import random
import sys

from functions import *
from init import enemy, turn

# initialize the board and start the game
board = create_board()
print(board)
game_over = False

pygame.init()

# case when the enemy is a regular player, ex: Player2
if enemy == PLAYER2:

    # drawing the board
    draw_board(board)
    pygame.display.update()

    while not game_over:
        for event in pygame.event.get():
            # handle the event when you close the game through the exit button
            if event.type == pygame.QUIT:
                sys.exit()

            # handle the event when the player can see his turn above the board
            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, COLORBLACK, (0, 0, width, SQUARESIZE))
                pos_x = event.pos[0]
                if turn == PLAYER1:
                    pygame.draw.circle(screen, COLORRED, (pos_x, int(SQUARESIZE / 2)), RADIUS)
                elif turn == PLAYER2:
                    pygame.draw.circle(screen, COLORYELLOW, (pos_x, int(SQUARESIZE / 2)), RADIUS)
            pygame.display.update()

            # handle the clicking event
            if event.type == pygame.MOUSEBUTTONDOWN:
                #  Player1 - regular player
                if turn == PLAYER1:
                    pos_x = event.pos[0]
                    column = int(math.floor(pos_x / SQUARESIZE))

                    if is_valid_location(board, column):
                        my_row = get_empty_row(board, column)
                        put_piece(board, my_row, column, PLAYER1_PIECE)

                        if winning_conditions(board, 1):
                            print("Player1 won the game.")
                            game_over = True
                            break
                        print_board(board)
                        draw_board(board)
                        turn = PLAYER2

                #  Player2 - regular player
                elif turn == PLAYER2:
                    pos_x = event.pos[0]
                    column = int(math.floor(pos_x / SQUARESIZE))

                    if is_valid_location(board, column):
                        my_row = get_empty_row(board, column)
                        put_piece(board, my_row, column, PLAYER2_PIECE)

                        if winning_conditions(board, 2):
                            print("Player2 won the game.")
                            game_over = True
                            break
                    print_board(board)
                    draw_board(board)
                    turn = PLAYER1

# case when the enemy is a AI
if enemy == AI:

    # drawing the board
    draw_board(board)
    pygame.display.update()

    while not game_over:
        for event in pygame.event.get():
            # handle the event when you close the game through the exit button
            if event.type == pygame.QUIT:
                sys.exit()

            # handle the event when the player can see his turn above the board
            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, COLORBLACK, (0, 0, width, SQUARESIZE))
                pos_x = event.pos[0]
                if turn == PLAYER1 or turn == PLAYER2:
                    pygame.draw.circle(screen, COLORRED, (pos_x, int(SQUARESIZE / 2)), RADIUS)
                elif turn == AI:
                    continue
            pygame.display.update()

            #  Player1/2 - regular player
            if turn == PLAYER1 or turn == PLAYER2:
                #  Player1/2 - regular player
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos_x = event.pos[0]
                    column = int(math.floor(pos_x / SQUARESIZE))

                    if is_valid_location(board, column):
                        my_row = get_empty_row(board, column)
                        put_piece(board, my_row, column, PLAYER1_PIECE)

                        if winning_conditions(board, 1):
                            print("Player1 won the game.")
                            game_over = True
                            break
                        print_board(board)
                        draw_board(board)
                        turn = AI

            #  Player2 - AI
            elif turn == AI:
                # column = random.randint(0, COLUMN_COUNT - 1)
                output_score, column = minmax_algorithm(board, 3, True)

                if is_valid_location(board, column):
                    my_row = get_empty_row(board, column)
                    put_piece(board, my_row, column, AI_PIECE)

                    if winning_conditions(board, 3):
                        print("AI won the game.")
                        game_over = True
                        break
                print_board(board)
                draw_board(board)
                turn = PLAYER1
