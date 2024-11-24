from constants import *
import pygame
from board import Board
from drag import Dragger

class Game:

    def __init__(self):
        self.board = Board()
        self.dragger = Dragger() # nuk e di pse e futa ktu
        self.is_white_turn = True
        pass


    def show_bg(self, surface):
        for row in range(8):
            for col in range(8):
                if (row + col) % 2 == 0:
                    color = (234, 235, 200) #light green
                else:
                    color = (119, 154, 88) #dark green

                rect = (col*SQSIZE, row*SQSIZE, SQSIZE, SQSIZE)

                pygame.draw.rect(surface, color, rect)

    def show_pieces(self, surface):
        for row in range(8):
            for col in range(8):
                square = self.board.squares[row][col]

                if square.has_piece():
                    piece = square.piece
                    if piece is not self.dragger.piece:
                        img = pygame.image.load(piece.image_path)
                        img_center = col*SQSIZE + SQSIZE//2, row*SQSIZE + SQSIZE//2
                        texture_rect = img.get_rect(center = img_center)
                        surface.blit(img, texture_rect)

    
    def show_moves(self, surface):
        if self.dragger.dragging:
            piece = self.dragger.piece

            valid_moves =  piece.get_valid_moves(self.board.squares)

            for position in valid_moves:
                print(position.row)
                print(position.col)
                color = '#C86464'

                rect = (position.col*SQSIZE, position.row*SQSIZE, SQSIZE, SQSIZE)

                pygame.draw.rect(surface, color, rect)


    def next_turn(self):
        self.is_white_turn = False if self.is_white_turn else True
       

        

