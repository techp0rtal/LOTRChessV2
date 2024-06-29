#I like chess and Lord of the Rings. This combines them both and makes a fun game! :D
# P.S. This project will heavily use pygame
# Step 1: We'll start by making the board itself, and have it pop up with dimensions we specify when you run the program.
import pygame
#from pygame.examples.go_over_there import screen
pygame.init()
WIDTH = 1000
HEIGHT = 900
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('LOTR Chess')
font = pygame.font.Font('freesansbold.ttf', 20)
big_font = pygame.font.Font('freesansbold.ttf', 50)
timer = pygame.time.Clock()
fps = 60
# game variables and images
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn','pawn','pawn','pawn','pawn','pawn','pawn']
white_locations = [(0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0),
                   (0,1), (1,1), (2,1), (3,1), (4,1), (5,1), (6,1), (7,1)]
black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn','pawn','pawn','pawn','pawn','pawn','pawn']
black_locations = [(0,7), (1,7), (2,7), (3,7), (4,7), (5,7), (6,7), (7,7),
                   (0,6), (1,6), (2,6), (3,6), (4,6), (5,6), (6,6), (7,6)]
captured_pieces_white = []
captured_pieces_black = []
'''
In chess, a turn/move is only "completed" when both players have made their moves. 
(The only exception to this rule is when White plays a move that ends the game.) 
So now we create a variable called 'turn_step' which will keep track of the 4 phases of each turn:
0- white's turn, no selection.
1- white's turn, piece selected.
2- black's turn, no selection.
3- black's turn, piece selected.
This variable will have 2 jobs: 
1. To keep track of which of the 4 phases we are in in the game (and which player is currently active).
2. To keep track of what valid moves are available on the board (which can be displayed on the board w/dots).
'''
turn_step = 0
'''
# Now we want a variable for whatever piece is actively selected. When you pick a piece, it wll keep track of what index in that list it is, by storing it in that
selection variable. And when no piece is selected, we'll just use a large number like 100 bc it's a large enough number that won't be on the board.
be an actual index.
'''
selection = 100
# Once we select a piece, the variable 'valid_moves' checks the number of valid moves
valid_moves = []
# load in game piece images, which will be their LOTR versions (king, queen, bishop, knight, rook, pawn)
#NOTE: make sure the images are square  (that is identical dimensions for both width and height like 1080x1080)
black_queen = pygame.image.load('Images/black pieces/b queen.jpg')
#Now we scale the images to fit the board tile size. If you want bigger than 80,80, need a bigger board and vice versa
black_queen = pygame.transform.scale(black_queen, (80,80))
#Now we need an even smaller version, that will be on the side of the game to represent the captured pieces.
black_queen_small = pygame.transform.scale(black_queen, (45,45))
black_king = pygame.image.load('Images/black pieces/b king.jpg')
black_king = pygame.transform.scale(black_king, (80, 80))
black_king_small = pygame.transform.scale(black_king, (45, 45))
black_rook = pygame.image.load('Images/black pieces/b rook.jpg')
black_rook = pygame.transform.scale(black_rook, (80, 80))
black_rook_small = pygame.transform.scale(black_rook, (45, 45))
black_bishop = pygame.image.load('Images/black pieces/b bishop.jpg')
black_bishop = pygame.transform.scale(black_bishop, (80, 80))
black_bishop_small = pygame.transform.scale(black_bishop, (45, 45))
black_knight = pygame.image.load('Images/black pieces/b knight.jpg')
black_knight = pygame.transform.scale(black_knight, (80, 80))
black_knight_small = pygame.transform.scale(black_knight, (45, 45))
black_pawn = pygame.image.load('Images/black pieces/b pawn.jpg')
black_pawn = pygame.transform.scale(black_pawn, (65, 65))
black_pawn_small = pygame.transform.scale(black_pawn, (45, 45))
#Now the white pieces. Note: the pawns' size is smaller on purpose.
white_queen = pygame.image.load('Images/white pieces/w queen.jpg')
white_queen = pygame.transform.scale(white_queen, (80, 80))
white_queen_small = pygame.transform.scale(white_queen, (45, 45))
white_king = pygame.image.load('Images/white pieces/w king.jpg')
white_king = pygame.transform.scale(white_king, (80, 80))
white_king_small = pygame.transform.scale(white_king, (45, 45))
white_rook = pygame.image.load('Images/white pieces/w rook.jpg')
white_rook = pygame.transform.scale(white_rook, (80, 80))
white_rook_small = pygame.transform.scale(white_rook, (45, 45))
white_bishop = pygame.image.load('Images/white pieces/w bishop.jpg')
white_bishop = pygame.transform.scale(white_bishop, (80, 80))
white_bishop_small = pygame.transform.scale(white_bishop, (45, 45))
white_knight = pygame.image.load('Images/white pieces/w knight.jpg')
white_knight = pygame.transform.scale(white_knight, (80, 80))
white_knight_small = pygame.transform.scale(white_knight, (45, 45))
white_pawn = pygame.image.load('Images/white pieces/w pawn.jpg')
white_pawn = pygame.transform.scale(white_pawn, (65, 65))
white_pawn_small = pygame.transform.scale(white_pawn, (45, 45))
'''
IMPORTANT: When we want to draw our pieces on the board, we will need a list that will
associate each piece's individual name with it's image by using an index.
Thus, it is important to keep the order/indexes of each string in piece_list and white_images and black_images
We'll call it "small_white_images" and "small_black_images"
'''
white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small,
                      white_rook_small, white_bishop_small]
black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small,
                      black_rook_small, black_bishop_small]
piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']
#check variables/flashing counter
'''
Now we need a list that is going to be strings for each piece 
that will have the same index for the image for each piece. 
'''

#time to draw the main game board

def draw_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        #now we need to offset the rows bc white and black squares change color
        if row % 2 == 0:
            pygame.draw.rect(screen, 'light gray', [600 - (column * 200), row * 100, 100, 100])
            #^^ We need a little space to the right, where our captured pieces can go.
        else:
            pygame.draw.rect(screen, 'light gray', [700-(column * 200), row * 100, 100, 100])
        pygame.draw.rect(screen, 'gray', [0, 800, WIDTH, 100])
        pygame.draw.rect(screen, 'gold', [0, 800, WIDTH, 100], 5) #this draws the gold rectangle on the bottom of screen
        pygame.draw.rect(screen, 'gold', [800, 0, 200, HEIGHT], 5) #this draws the gold rectangle on the right
        status_text = ['White: Select a piece to move!', "White: Select a destination!",
                    'Black: Select a piece to move!', "Black: Select a destination!",]
        screen.blit(big_font.render(status_text[turn_step], True, 'black'), (20, 820))
        for i in range(9): #this will draw lines between our squares to add a nice border.
            pygame.draw.line(screen, 'black', (0, 100 * i), (800, 100 * i), 2)  #draws horizontal lines
            pygame.draw.line(screen, 'black', (100 * i, 0), (100 * i, 800), 2)  #draws vertical lines (by inverting the horizontal values)

#Draws pieces out on the board.
def draw_pieces():
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i]) #to not what image we need to draw on the screen, we need an index value that will tell us which piece image to use
        if white_pieces[i] == 'pawn': #we have to do a seperate one for the pawns bc they're different sizes
            screen.blit(white_pawn, (white_locations[i][0] * 100 + 22, white_locations[i][1] * 100 + 30)) #we need this to center the pawn image since it's smaller
        else:
            screen.blit(white_images[index], (white_locations[i][0] * 100 + 10, white_locations[i][1] * 100 + 10))
        #now let's highlight a piece when it's selected. if turn step < 2, then it's white player's turn. if >= 2, it's black's turn, and we will use blue.
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, 'red', [white_locations[i][0] * 100 + 1, white_locations[i][1] * 100 + 1, 100, 100], 2) #to test this, set selection = 10

    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i]) #to not what image we need to draw on the screen, we need an index value that will tell us which piece image to use
        if black_pieces[i] == 'pawn': #we have to do a seperate one for the pawns bc they're different sizes
            screen.blit(black_pawn, (black_locations[i][0] * 100 + 22, black_locations[i][1] * 100 + 30)) #we need this to center the pawn image since it's smaller
        else:
            screen.blit(black_images[index], (black_locations[i][0] * 100 + 10, black_locations[i][1] * 100 + 10))
        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen, 'blue', [black_locations[i][0] * 100 + 1, black_locations[i][1] * 100 + 1, 100, 100], 2)

# function to check all pieces' valid options on the board. will only update when a piece moves/is captured. VERY important for checking if the king is in check
def check_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = []
    for i in range((len(pieces))):
        location = locations[i]
        piece = pieces[i]
        #this next part will check every possible move for every possible piece.
        if piece == 'pawn':
            moves_list = check_pawn(location, turn)
            ''' elif piece == 'rook':
            moves_list = check_rook(location, turn)
        elif piece == 'knight':
            moves_list = check_knight(location, turn)
        elif piece == 'bishop':
            moves_list = check_bishop(location, turn)
        elif piece == 'queen':
            moves_list = check_queen(location, turn)
        elif piece == 'king':
            moves_list = check_king(location, turn)'''

        #we just got a list of available moves for each piece. now let's add them together
        all_moves_list.append(moves_list)
    return all_moves_list

#check valid pawn moves. we will do this for all pieces
def check_pawn(position, color):
    moves_list = []
    if color == 'white':
        if (position[0], position [1] + 1) not in white_locations and \
                (position[0], position[1] + 1) not in black_locations and position[1] < 7: #gotta make sure it doesn't move into a black piece or off the bottom of the board)
            moves_list.append((position[0], position[1] + 1))
        if (position[0], position [1] + 2) not in white_locations and \
                (position[0], position[1] + 2) not in black_locations and position[1] == 1: #this is for the starting move where a pawn can move 2 spaces
            moves_list.append((position[0], position[1] + 2))
        #now let's make the pawns' diagonal attack move
        if (position[0] + 1, position [1] + 1) in black_locations:
            moves_list.append((position[0] + 1, position[1] + 1))
        #^^that only checks the diagonal attack for ONE side. so we need to do it again for the other side (left). do a -1 instead to do this.
        if (position[0] - 1, position [1] + 1) in black_locations:
            moves_list.append((position[0] - 1, position[1] + 1))
        '''now we need to do an else for the black pawns because their movement is opposite of what we just checked. they go up the board not down.
        can do an else statement bc there's only 2 colors of pieces: white or black.'''
    else:
        if (position[0], position[1] - 1) not in white_locations and \
                (position[0], position[1] - 1) not in black_locations and position[1] > 0:  # gotta make sure it doesn't move into a black piece or off the bottom of the board)
            moves_list.append((position[0], position[1] + 1))
        if (position[0], position[1] + 2) not in white_locations and \
                (position[0], position[1] + 2) not in black_locations and position[
            1] == 1:  # this is for the starting move where a pawn can move 2 spaces
            moves_list.append((position[0], position[1] + 2))
        # now let's make the pawns' diagonal attack move
        if (position[0] + 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] + 1, position[1] - 1))
        # ^^that only checks the diagonal attack for ONE side. so we need to do it again for the other side (left). do a -1 instead to do this.
        if (position[0] - 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] - 1, position[1] - 1))
    return moves_list



#draws valid moves on screen
def draw_valid(moves):
    if turn_step < 2:
        color = 'red'
    else:
       color = 'blue'
    for i in range(len(moves)):
        pygame.draw.circle(screen, color, (moves[i][0] * 100 + 50, moves[i][1] *100 +500), 5)



#check for valid moves for just selected piece
def check_valid_moves():
    if turn_step < 2:
        options_list = white_options
    else:
        options_list = black_options
    valid_options = options_list[selection]
    return valid_options




# main game loop
black_options = check_options(black_pieces, black_locations,'black') #checks the options of each piece and all their valid moves. the hardest part of programming chess
white_options = check_options(white_pieces, white_locations,'white')

run = True
while run:
    timer.tick(fps)
    screen.fill('dark gray')
    draw_board()
    draw_pieces()
    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves)



    #event handling (getting all your inputs, key board, mouse, etc)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x_coord = event.pos[0] // 100 #pygame has event.pos which tells us the x,y coordinate of the mouse click on the grid, but on our grid each square is 100 wide, so div x by 100
            y_coord = event.pos[1] // 100 #same thing for y
            clicks_coords = (x_coord, y_coord) #useful to have as a tuple because that's how we have all the coordinates of the pieces stored
            #now we will have a bit of variation depending on if it's white's or black's turn
            if turn_step <=1:
                if clicks_coords in white_locations:
                    selection = white_locations.index(clicks_coords)
                    if turn_step == 0:
                        turn_step = 1
                if clicks_coords in valid_moves and selection != 100:
                    white_locations[selection] = clicks_coords
                    if clicks_coords in black_locations:
                        black_piece =black_locations.index(clicks_coords) #checks what piece we just took out
                        captured_pieces_white.append(black_pieces[black_piece]) #black piece is an index, and black pieces is the list of all the pieces. we adding piece we just captured for the white player
                        black_pieces.pop(black_piece)
                        black_locations.pop(black_piece) #this is removing the piece the white piece just landed on from our pieces list and locatoins' list and adding it to the list of captured pieces
                    black_options = check_options(black_pieces, black_locations, 'black') #checks the options of each piece and all their valid moves. the hardest part of programming chess
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step = 2
                    selection = 100
                    valid_moves = []
            #now what to do if it's black's turn?
            if turn_step > 1:
                if clicks_coords in black_locations:
                    selection = black_locations.index(clicks_coords)
                    if turn_step == 2:
                        turn_step = 3
                if clicks_coords in valid_moves and selection != 100:
                    black_locations[selection] = clicks_coords
                    if clicks_coords in white_locations:
                        white_piece =white_locations.index(clicks_coords) #checks what piece we just took out
                        captured_pieces_black.append(white_pieces[white_piece]) #black piece is an index, and black pieces is the list of all the pieces. we adding piece we just captured for the white player
                        white_pieces.pop(white_piece)
                        white_locations.pop(white_piece) #this is removing the piece the white piece just landed on from our pieces list and locatoins' list and adding it to the list of captured pieces
                    black_options = check_options(black_pieces, black_locations, 'black') #checks the options of each piece and all their valid moves (doesn't change)
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step = 0
                    selection = 100
                    valid_moves = []





    pygame.display.flip()
pygame.quit()