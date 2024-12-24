from constants import *
import pygame
import sys
from game import Game
from board import Board
from graphics import Graphics


class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('Chess')
        self.game = Game()
        self.graphics = Graphics()

    def mainloop(self):

        screen = self.screen
        game = self.game
        board = self.game.board
        graphics = self.graphics
        dragger = self.graphics.dragger
        
        run = True
        while run:
            #show methods
            graphics.show_bg(screen)
            if dragger.dragging:
                graphics.show_moves(screen, game.get_valid_game_moves(dragger.piece))
            graphics.show_pieces(screen, board.squares)
            if dragger.dragging:
                dragger.update_blit(screen)
                
            if game.game_over:
                graphics.show_game_over(screen, game.is_white_turn)
                
            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)

                    clicked_row = dragger.mouseY // SQSIZE
                    clicked_col = dragger.mouseX // SQSIZE

                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece
                        if game.is_white_turn == piece.is_white:
                            dragger.save_initial(event.pos)
                            dragger.drag_piece(piece)
                            #show moves
                            graphics.show_bg(screen)
                            if dragger.dragging:
                                graphics.show_moves(screen, game.get_valid_game_moves(dragger.piece))
                            graphics.show_pieces(screen, board.squares)
                     
                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        #show methods
                        graphics.show_bg(screen)
                        graphics.show_moves(screen, game.get_valid_game_moves(dragger.piece))
                        graphics.show_pieces(screen, board.squares)
                        dragger.update_blit(screen)
                        


                elif event.type == pygame.MOUSEBUTTONUP:
                    dragger.update_mouse(event.pos)
                    if game.move_piece(dragger.initial_position, dragger.current_position):
                        game.next_turn()

                    if game.is_checkmate():
                        game.game_over = True
                        graphics.show_game_over(screen, game.is_white_turn)

                    dragger.undrag_piece()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        game.reset()
                        game = self.game
                        board = self.game.board
                        graphics = self.graphics
                        dragger = self.graphics.dragger
                    

                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


        


main = Main()
main.mainloop()
        

