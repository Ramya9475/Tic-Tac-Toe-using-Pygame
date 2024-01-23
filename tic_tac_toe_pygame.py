import pygame, sys
import numpy as np
pygame.init()



width = 600
height = width
line_width = 15
board_rows = 3
board_columns = 3
square_size = width//board_columns
space = 55
circle_radius = 60
circle_width = 15
#rgb : red green blue
red = (255, 0, 0)
bg_color = (28, 170, 156)
line_color = (23,145,135)
circle_color = (239, 231, 200)
cross_color = (66,66,66)


screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("TIC TAC TOE")
screen.fill(bg_color)

#board
board = np.zeros((board_rows, board_columns))
print(board)

#pygame.draw.line(screen , red , (10,10), (300,300), 10)
def draw_figures():
    for row in range(board_rows):
        for col in range(board_columns):
            if board[row][col] == 1:
                pygame.draw.circle(screen, circle_color, (int(col * square_size + square_size // 2), int(row * square_size + square_size // 2)), min(square_size, square_size) // 2 - space, circle_width)
            elif board[row][col] == 2:
                line_width = int(square_size / 8)  # Adjust this factor based on your preferences
                pygame.draw.line(screen, cross_color, (col * square_size + space, row * square_size + space), (col * square_size + square_size - space, row * square_size + square_size - space), line_width)
                pygame.draw.line(screen, cross_color, (col * square_size + space, row * square_size + square_size - space), (col * square_size + square_size - space, row * square_size + space), line_width)



def draw_lines():
    #1st horizontal line
    pygame.draw.line(screen, line_color, (0,square_size), (width,square_size), line_width)
    #2nd horizontal line
    pygame.draw.line(screen, line_color, (0, 2*square_size), (width, 2*square_size), line_width)

    #1st vertical line
    pygame.draw.line(screen, line_color, (square_size,0), (square_size, height), line_width)
    #2nd vertical line
    pygame.draw.line(screen, line_color, (2*square_size,0), (2*square_size, height), line_width)

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] ==0

def is_board_full():
    for row in range(board_rows):
        for col in range(board_columns):
            if board[row][col]==0:
                return False
    return True

def check_win(player):
    #vertical win check
    for col in range(board_columns):
        if board[0][col]==player and board[1][col] == player and board[2][col] == player :
            draw_vertical_winning_line(col, player)
            return True

    #horizontal win check
    for row in range(board_rows):
        if board[row][0] == player and board[row][1] == player and board[row][2]==player:
            draw_horizontal_winning_line(row,player)

    #asc diagonal win check
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonals(player)

    #desc diagonal win check
    if board[0][0] == player and  board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True

    return False

def draw_vertical_winning_line(col, player):
    posX = col*square_size+square_size//2
    if player == 1:
        color = circle_color
    elif player == 2:
        color = cross_color

    pygame.draw.line(screen, color, (posX,15), (posX,height-15),15)


def draw_horizontal_winning_line(row, player):
    posY = row * square_size + square_size // 2
    if player == 1:
        color = circle_color
    elif player == 2:
        color = cross_color

    pygame.draw.line(screen, color, (15, posY), (width - 15, posY), 15)
def draw_asc_diagonals(player):
    if player == 1:
        color = circle_color
    elif player == 2:
        color = cross_color

    pygame.draw.line(screen , color , (15 , height-15) , (width-15 , 15) , 15)
def draw_desc_diagonal(player):
    if player == 1:
        color = circle_color
    elif player == 2:
        color = cross_color

    pygame.draw.line(screen, color, (15, 15), (width - 15, height - 15), 15)
def restart():
    screen.fill(bg_color)
    draw_lines()
    player = 1
    for row in range(board_rows):
        for col in range(board_columns):
            board[row][col] = 0

def display_result(result):
    pygame.draw.rect(screen, (255, 255, 255), (width // 4, height // 4, width // 2, height // 2))
    font = pygame.font.Font(None, 36)
    text = font.render(result, True, (0,0,0))
    text_rect = text.get_rect(center=(width // 2, height // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(3000)



draw_lines()

player = 1
game_over = False
result_displayed = False
#mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if not game_over:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = event.pos
                clicked_row = mouseY // square_size
                clicked_col = mouseX // square_size

                if available_square(clicked_row, clicked_col):
                    mark_square(clicked_row, clicked_col, player)
                    if check_win(player):
                        result_displayed = True
                        game_over = True
                        result = f"Player {player} wins!"
                    elif is_board_full():
                        result_displayed = True
                        game_over = True
                        result = "It's a tie!"
                    else:
                        player = 3 - player  # Switch player (1 -> 2, 2 -> 1)

                    draw_figures()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart()
                    game_over = False
                    player = 1

    if result_displayed:
        display_result(result)
        result_displayed = False

    pygame.display.update()