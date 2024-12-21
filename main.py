from constants import *
import pygame
import sys
from game import Game
from board import Board


class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('Chess')
        self.game = Game()

    def mainloop(self):

        screen = self.screen
        game = self.game
        board = self.game.board
        dragger = self.game.dragger
        
        run = True
        while run:
            #show methods
            game.show_bg(screen)
            game.show_moves(screen)
            game.show_pieces(screen)

            if dragger.dragging:
                dragger.update_blit(screen)
                
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
                            game.show_bg(screen)
                            game.show_moves(screen)
                            game.show_pieces(screen)
                        
                     
                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        #show methods
                        game.show_bg(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)
                        dragger.update_blit(screen)
                        


                elif event.type == pygame.MOUSEBUTTONUP:
                    dragger.update_mouse(event.pos)
                    if game.move_piece(dragger.initial_position, dragger.current_position):
                        game.next_turn()
                    print(f'Initial Row: {dragger.initial_position.row}')
                    print(f'Initial col: {dragger.initial_position.col}')
                    print(f'current row: {dragger.current_position.row}')
                    print(f'current col: {dragger.current_position.col}')


                    dragger.undrag_piece()
                    

                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


        


main = Main()
main.mainloop()
        

