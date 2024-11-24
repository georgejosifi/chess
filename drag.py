
from constants import *
import pygame
from position import Position
class Dragger:

    def __init__(self):
        self.mouseX = 0
        self.mouseY = 0
        self.current_position = Position(self.mouseY // SQSIZE, self.mouseX // SQSIZE)
        self.initial_position = Position(0,0)
        self.piece = None
        self.dragging = False
    

    def update_blit(self, surface):
        img = pygame.image.load(self.piece.image_path)
        img_center = self.mouseX, self.mouseY
        texture_rect = img.get_rect(center = img_center)
        surface.blit(img, texture_rect)


    def update_mouse(self, pos):
        self.mouseX, self.mouseY = pos
        self.current_position = Position(self.mouseY // SQSIZE, self.mouseX // SQSIZE)


    def save_initial(self, pos):
        initial_row = pos[1] // SQSIZE
        initial_col = pos[0] // SQSIZE
        self.initial_position = Position(initial_row, initial_col)

    def drag_piece(self, piece):
        self.piece = piece
        self.dragging = True

    def undrag_piece(self):
        self.piece = None
        self.dragging = False
