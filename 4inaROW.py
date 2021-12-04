from functions import *

# initialize the board and start the game
board = create_board()
print(board)
game_over = False
turn = 0

pygame.init()

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
            if turn == 0:
                pygame.draw.circle(screen, COLORRED, (pos_x, int(SQUARESIZE / 2)), RADIUS)
            else:
                pygame.draw.circle(screen, COLORYELLOW, (pos_x, int(SQUARESIZE / 2)), RADIUS)
        pygame.display.update()

        # handle the clicking event
        if event.type == pygame.MOUSEBUTTONDOWN:
            #  Player1
            if turn == 0:
                pos_x = event.pos[0]
                column = int(math.floor(pos_x / SQUARESIZE))

                if is_valid_location(board, column):
                    my_row = get_empty_row(board, column)
                    put_piece(board, my_row, column, 1)

            #  Player2
            else:
                pos_x = event.pos[0]
                column = int(math.floor(pos_x / SQUARESIZE))

                if is_valid_location(board, column):
                    my_row = get_empty_row(board, column)
                    put_piece(board, my_row, column, 2)

            print_board(board)
            draw_board(board)
            turn += 1
            turn = turn % 2
