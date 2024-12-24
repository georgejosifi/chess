import pygame
from constants import *
from drag import Dragger



class Graphics:
    
    def __init__(self):
        self.dragger = Dragger()

    def show_bg(self, surface):
        for row in range(8):
            for col in range(8):
                if (row + col) % 2 == 0:
                    color = (234, 235, 200) #light green
                else:
                    color = (119, 154, 88) #dark green

                rect = (col*SQSIZE, row*SQSIZE, SQSIZE, SQSIZE)

                pygame.draw.rect(surface, color, rect)


    def show_pieces(self, surface, squares):
        for row in range(8):
            for col in range(8):
                square = squares[row][col]

                if square.has_piece():
                    piece = square.piece
                    if piece is not self.dragger.piece:
                        img = pygame.image.load(piece.image_path)
                        img_center = col*SQSIZE + SQSIZE//2, row*SQSIZE + SQSIZE//2
                        texture_rect = img.get_rect(center = img_center)
                        surface.blit(img, texture_rect)


    def show_moves(self, surface, valid_moves):
            for position in valid_moves:
                print(position.row)
                print(position.col)
                color = '#C86464'

                rect = (position.col*SQSIZE, position.row*SQSIZE, SQSIZE, SQSIZE)

                pygame.draw.rect(surface, color, rect)


    def show_game_over(self, surface, is_white_turn):
        winner = "Black" if is_white_turn else "White"
        rect = (WIDTH/2 - 1.5*SQSIZE, HEIGHT/2 - SQSIZE, 3*SQSIZE, 2*SQSIZE)
        pygame.draw.rect(surface, 'black', rect)
        font = pygame.font.Font(None, 25)
        message = f'{winner} won the game'
        text = font.render(message, True, 'white')
        text_rect = text.get_rect(center = (WIDTH/2 - 0.2*SQSIZE, HEIGHT/2 - 0.5*SQSIZE))
        surface.blit(text, text_rect)
        restart_message = 'Press R to restart the game'
        restart_text = font.render(restart_message, True, 'white')
        restart_text_rect = text.get_rect(center = (WIDTH/2- 0.2*SQSIZE, HEIGHT/2 + 0.5*SQSIZE))
        surface.blit(restart_text, restart_text_rect)