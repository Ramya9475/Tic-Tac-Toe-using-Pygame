# TIC - TAC - TOE using Pygame

### Initialization:
Pygame is initialized.
Constants for the game window and board are set, such as width, height, line width, board rows, board columns, square size, space, circle radius, and colors.
Pygame screen and window caption are set.

### Board Representation:
A 3x3 NumPy array (board) is used to represent the state of the Tic Tac Toe board. It is initially filled with zeros.

### Drawing Functions:
draw_figures(): Draws circles and crosses on the board based on the current state. 
draw_lines(): Draws horizontal and vertical lines to create the Tic Tac Toe grid.

### Game Logic Functions:
mark_square(row, col, player): Marks a square on the board with the current player's symbol (1 for circle, 2 for cross).
available_square(row, col): Checks if a square is available (not marked by any player).
is_board_full(): Checks if the entire board is filled.
check_win(player): Checks for a win condition for the given player (horizontal, vertical, and diagonal).

### Drawing Winning Lines:
Functions like draw_vertical_winning_line, draw_horizontal_winning_line, draw_asc_diagonals, and draw_desc_diagonal are used to draw lines when a player wins.

### Restart Function:
restart(): Clears the screen, redraws the lines, and resets the board for a new game.

### Displaying Results:
display_result(result): Displays the result (winner or tie) in a rectangular box at the center of the screen.

### Main Game Loop:
The main loop continuously checks for user input events.
If the game is not over, it responds to mouse clicks to mark squares and updates the game state.
Pressing the 'r' key restarts the game.
If the game is over, it displays the result for a brief period before allowing a restart.
