import sys
import numpy
import pygame
import math
numbers_of_rows=6
numbers_of_columns=7
blue=(0,0,255)
black=(0,0,0)
red=(255,0,0)
yellow=(255,255,0)
def make_board():
    board=numpy.zeros((numbers_of_rows,numbers_of_columns))
    return board
def drop_piece(board,row,col,piece):
    board[row][col]=piece
def valid_loc(board,col):
    return board[numbers_of_rows-1][col]==0
def get_next_row(board,col):
    for r in range(0,6):
        if board[r][col]==0:
            return r
def win(board,piece):
    # horizontal winning
    for col in range(numbers_of_columns-3):
        for row in range(numbers_of_rows):
            if board[row][col]==piece and board[row][col+1]==piece and board[row][col+2]==piece and board[row][col+3]==piece:
                return True
    for row in range(numbers_of_rows-3):
        for col in range(numbers_of_columns):
            if board[row][col]==piece and board[row+1][col]==piece and board[row+2][col]==piece and board[row+3][col]==piece:
                return True
    for col in range(numbers_of_columns-3):
        for row in range(numbers_of_rows-3):
            if board[row][col]==piece and board[row+1][col+1]==piece and board[row+2][col+2]==piece and board[row+3][col+3]==piece:
                return True
    for col in range(numbers_of_columns-3):
        for row in range(3,numbers_of_rows):
            if board[row][col]==piece and board[row-1][col+1]==piece and board[row-2][col+2]==piece and board[row-3][col+3]==piece:
                return True
b=make_board()
def draw_board(board):
    for col in range(numbers_of_columns):
        for row in range(numbers_of_rows):
            pygame.draw.rect(screen,blue,(col*square_size,row*square_size+square_size,square_size,square_size))
            pygame.draw.circle(screen,black,(int(col*square_size+square_size/2),int(row*square_size+square_size+square_size/2)),radius)
    for col in range(numbers_of_columns):
        for row in range(numbers_of_rows):
            if board[row][col]==1:
                pygame.draw.circle(screen, red, (int(col * square_size + square_size / 2),height- int(row * square_size  + square_size / 2)),radius)
            elif board[row][col]==2:
                pygame.draw.circle(screen, yellow, (int(col * square_size + square_size / 2),height- int(row * square_size + square_size / 2)),radius)
    pygame.display.update()
def print_fliped(b):
    print(numpy.flip(b,0))
print_fliped(b)


game_over=False
T=0
pygame.init()
square_size=100
width=square_size*numbers_of_columns
height=square_size*(numbers_of_rows+1)
size=(width,height)
radius=int((square_size/2)-5)
screen=pygame.display.set_mode(size)
f=pygame.font.SysFont("Monospace",75)

draw_board(b)
pygame.display.update()
c=0
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==pygame.MOUSEMOTION:
            pygame.draw.rect(screen,black,(0,0,width,square_size))
            posx=event.pos[0]
            if T==0:
                pygame.draw.circle(screen, red, (posx, int(square_size / 2)), radius)
            else:
                pygame.draw.circle(screen, yellow, (posx, int(square_size / 2)), radius)
        pygame.display.update()
        if event.type==pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, black, (0, 0, width, square_size))
            if T%2==0:
                pygame.draw.circle(screen,red,(posx,int(square_size/2)),radius)
                posx=event.pos[0]
                print(posx)
                column=int(math.floor(posx/square_size))
                if valid_loc(b,column):
                    row=get_next_row(b,column)
                    drop_piece(b,row,column,1)
                    if win(b,1):
                        pygame.draw.rect(screen, black, (0, 0, width, square_size))
                        pygame.display.update()
                        l=f.render("Player 1 wins ",1,red)
                        screen.blit(l,(40,10))
                        game_over=True
            else:
                posx = event.pos[0]
                column = int(math.floor(posx/square_size))
                if valid_loc(b, column):
                    row = get_next_row(b, column)
                    drop_piece(b, row, column, 2)
                    if win(b, 2):

                        l = f.render("Player 2 wins ", 1, yellow)
                        screen.blit(l, (40, 10))
                        game_over = True
            if not valid_loc(b,column):
                c+=1
                if(c==7):
                    x= f.render("no one wins", 1, blue)
                    screen.blit(x, (40, 10))
                    game_over=True
                    game_over=True
            T+=1
            draw_board(b)
            print_fliped(b)
            if game_over:
                pygame.time.wait(2500)
