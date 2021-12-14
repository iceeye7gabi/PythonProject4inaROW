import sys

from functions import *

from init import enemy, turn

from graphics import *

"""
initialize the board and start the game
"""
board = create_board()
print(board)
game_over = False
pygame.init()

"""
case when the enemy is a regular player, ex: Player2
"""
if enemy == PLAYER2:

    """
    drawing the board
    """
    draw_board(board)
    pygame.display.update()
    while not game_over:
        for event in pygame.event.get():
            """
            handle the event when you close the game through the exit button
            """
            if event.type == pygame.QUIT:
                sys.exit()

            """
            handle the event when the player can see his turn above the board
            """
            pygame.display.update()
            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, COLORBLACK, (0, 0, width, SQUARESIZE))
                pos_x = event.pos[0]
                if turn == PLAYER1:
                    show_player_turn(turn)
                    pygame.draw.circle(screen, COLORRED, (pos_x, int(SQUARESIZE / 2)), RADIUS)
                    if 0 < pos_x < 100:
                        pygame.draw.line(screen, COLORPINK, (50, 80), (50, 500), width = 3)
                        pygame.display.update()
                    else:
                        draw_board(board)
                    if 101 < pos_x < 200:
                        pygame.draw.line(screen, COLORPINK, (150, 80), (150, 500), width = 3)
                        pygame.display.update()
                    elif 201 < pos_x < 300:
                        pygame.draw.line(screen, COLORPINK, (250, 80), (250, 500), width = 3)
                        pygame.display.update()
                    elif 301 < pos_x < 400:
                        pygame.draw.line(screen, COLORPINK, (350, 80), (350, 500), width = 3)
                        pygame.display.update()
                    elif 401 < pos_x < 500:
                        pygame.draw.line(screen, COLORPINK, (450, 80), (450, 500), width = 3)
                        pygame.display.update()
                    elif 501 < pos_x < 600:
                        pygame.draw.line(screen, COLORPINK, (550, 80), (550, 500), width = 3)
                        pygame.display.update()
                    elif 601 < pos_x < 700:
                        pygame.draw.line(screen, COLORPINK, (650, 80), (650, 500), width = 3)
                        pygame.display.update()
                    elif 701 < pos_x < 800:
                        pygame.draw.line(screen, COLORPINK, (750, 80), (750, 500), width = 3)
                        pygame.display.update()

                    pygame.display.update()
                elif turn == PLAYER2:
                    show_player_turn(turn)
                    pygame.draw.circle(screen, COLORYELLOW, (pos_x, int(SQUARESIZE / 2)), RADIUS)
                    if 0 < pos_x < 100:
                        pygame.draw.line(screen, COLORPINK, (50, 80), (50, 500), width = 3)
                        pygame.display.update()
                    else:
                        draw_board(board)
                    if 101 < pos_x < 200:
                        pygame.draw.line(screen, COLORPINK, (150, 80), (150, 500), width = 3)
                        pygame.display.update()
                    elif 201 < pos_x < 300:
                        pygame.draw.line(screen, COLORPINK, (250, 80), (250, 500), width = 3)
                        pygame.display.update()
                    elif 301 < pos_x < 400:
                        pygame.draw.line(screen, COLORPINK, (350, 80), (350, 500), width = 3)
                        pygame.display.update()
                    elif 401 < pos_x < 500:
                        pygame.draw.line(screen, COLORPINK, (450, 80), (450, 500), width = 3)
                        pygame.display.update()
                    elif 501 < pos_x < 600:
                        pygame.draw.line(screen, COLORPINK, (550, 80), (550, 500), width = 3)
                        pygame.display.update()
                    elif 601 < pos_x < 700:
                        pygame.draw.line(screen, COLORPINK, (650, 80), (650, 500), width = 3)
                        pygame.display.update()
                    elif 701 < pos_x < 800:
                        pygame.draw.line(screen, COLORPINK, (750, 80), (750, 500), width = 3)
                        pygame.display.update()
            pygame.display.update()

            """
            handle the clicking event
            """
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Player1 - regular player
                if turn == PLAYER1:
                    pos_x = event.pos[0]
                    column = int(math.floor(pos_x / SQUARESIZE))
                    pygame.draw.rect(screen, COLORBLACK, (0, 0, width, SQUARESIZE))
                    pygame.draw.circle(screen, COLORYELLOW, (pos_x, int(SQUARESIZE / 2)), RADIUS)
                    show_player_turn(PLAYER2)
                    pygame.display.update()

                    if is_valid_location(board, column):
                        my_row = get_empty_row(board, column)
                        put_piece(board, my_row, column, PLAYER1_PIECE)

                        if winning_conditions(board, PLAYER1):
                            print("Player1 won the game.")
                            game_over = True
                            show_player1_win_screen()
                            print_board(board)
                            break
                        print_board(board)
                        draw_board(board)
                        turn = PLAYER2

                #  Player2 - regular player
                elif turn == PLAYER2:
                    pos_x = event.pos[0]
                    column = int(math.floor(pos_x / SQUARESIZE))
                    pygame.draw.rect(screen, COLORBLACK, (0, 0, width, SQUARESIZE))
                    pygame.draw.circle(screen, COLORRED, (pos_x, int(SQUARESIZE / 2)), RADIUS)
                    show_player_turn(PLAYER1)
                    pygame.display.update()

                    if is_valid_location(board, column):
                        my_row = get_empty_row(board, column)
                        put_piece(board, my_row, column, PLAYER2_PIECE)

                        if winning_conditions(board, PLAYER2):
                            print("Player2 won the game.")
                            game_over = True
                            show_player2_win_screen()
                            print_board(board)
                            break
                    print_board(board)
                    draw_board(board)
                    turn = PLAYER1
"""
case when the enemy is a AI
"""
if enemy == AI:

    """choose AI level screen"""
    show_ai_levels_screen()
    pygame.display.update()
    chosen_difficulty = 0
    level_ai = -1
    while not chosen_difficulty:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            """player has to click in order to choose AI level"""
            if event.type == pygame.MOUSEBUTTONDOWN:
                point = event.pos[1]
                if point < height / 3:
                    level_ai = 0
                if height / 3 < point < 2 * height / 3:
                    level_ai = 1
                if 2 * height / 3 < point < height:
                    level_ai = 2
                chosen_difficulty = 1

    """
    drawing the board
    """
    draw_board(board)
    pygame.display.update()

    while not game_over:
        for event in pygame.event.get():
            """
            handle the event when you close the game through the exit button
            """
            if event.type == pygame.QUIT:
                sys.exit()

            """
            handle the event when the player can see his turn above the board
            """
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
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos_x = event.pos[0]
                    column = int(math.floor(pos_x / SQUARESIZE))

                    if is_valid_location(board, column):
                        my_row = get_empty_row(board, column)
                        put_piece(board, my_row, column, PLAYER1_PIECE)

                        if winning_conditions(board, PLAYER1):
                            print("Player1 won the game.")
                            game_over = True
                            show_player1_win_screen()
                            print_board(board)
                            break
                        print_board(board)
                        draw_board(board)
                        turn = AI

            #  Player2 - AI
            elif turn == AI and not game_over:
                # Easy AI - Random Choice
                if level_ai == 0:
                    column = random.randint(0, COLUMN_COUNT - 1)
                # Medium AI - MinMax with depth = 3
                elif level_ai == 1:
                    output_score, column = minmax_algorithm(board, 3, True)
                # Hard AI - MinMax with alpha_beta pruning with depth = 5
                elif level_ai == 2:
                    output_score, column = minmax_algorithm_with_alpha_beta_pruning(board, 5, -math.inf, math.inf, True)
                else:
                    column = random.randint(0, COLUMN_COUNT - 1)

                if is_valid_location(board, column):
                    my_row = get_empty_row(board, column)
                    put_piece(board, my_row, column, AI_PIECE)

                    if winning_conditions(board, AI):
                        print("AI won the game.")
                        game_over = True
                        show_ai_win_screen()
                        print_board(board)
                        break
                print_board(board)
                draw_board(board)
                turn = PLAYER1
