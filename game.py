from constants import *
import copy
import pygame
from board import Board
from drag import Dragger
from piece import *

class Game:

    def __init__(self):
        self.board = Board()
        self.is_white_turn = True
        self.game_over = False


    def move_piece(self, start_position: Position, end_position: Position) -> bool:
        if (start_position.row >7 or start_position.row <0 or start_position.col > 7 
            or start_position.col<0 or end_position.row >7 or end_position.row <0 or end_position.col > 7 or end_position.col<0):
            return False
        
        piece = self.board.squares[start_position.row][start_position.col].piece
        if piece == None:
            print('Error: There is no piece in this square')
            return False
        
        valid_piece_moves = self.get_valid_game_moves(piece)
        is_valid_move = any(position.row == end_position.row and position.col == end_position.col for position in valid_piece_moves)
        if is_valid_move:
            self.board.move_piece(start_position, end_position)
            if isinstance(piece, Pawn) or isinstance(piece, King) or isinstance(piece, Rook):
                piece.has_moved = True
            
            if isinstance(piece, Pawn):
                self.pawn_promotion(piece, end_position)

            if isinstance(piece, King):
                if is_castling_move(start_position, end_position):
                    self.castle(start_position, end_position)
                    

            return True

        else:
            print("Error: Cannot move to that square")
            return False


    

    def pawn_promotion(self, pawn, end_position):
        if end_position.row == 0 or end_position.row == 7:
            end_square = self.board.squares[end_position.row][end_position.col]
            end_square.piece = Queen(pawn.is_white, False, end_square)



    def is_checkmate(self):
        for row in range(8):
            for col in range(8):
                current_square = self.board.squares[row][col]
                if current_square.has_team_piece(self.is_white_turn):
                    valid_moves = self.get_valid_game_moves(current_square.piece)
                    if valid_moves:
                        return False
                
        return True



    def in_check_move_filter(self, valid_moves, start_position, is_white):
        temp_board = copy.deepcopy(self.board)
        safe_moves  = []
        for end_position in valid_moves:
            captured_piece = temp_board.squares[end_position.row][end_position.col].piece
            temp_board.move_piece(start_position, end_position)
            if not self.is_king_in_check(temp_board, is_white):
                safe_moves.append(end_position)
            temp_board.undo_move(start_position, end_position, captured_piece)
            
        return safe_moves

            

    def is_king_in_check(self, board, is_white):
        for row in range(8):
            for col in range(8):
                if board.squares[row][col].has_rival_piece(is_white):
                    p = board.squares[row][col].piece
                    rival_moves = p.get_valid_moves(board.squares)
                    for moves in rival_moves:
                        end_square = board.squares[moves.row][moves.col]
                        if isinstance(end_square.piece, King):
                            return True
                
        return False
    

    def get_valid_game_moves(self, piece):
        return self.in_check_move_filter(piece.get_valid_moves(self.board.squares), piece.square.position, piece.is_white)
         

    
    def next_turn(self):
        self.is_white_turn = False if self.is_white_turn else True


    def castle(self, start_position, end_position):
        diff = end_position.col - start_position.col
        if diff > 0:
            start_position_of_rook, end_position_of_rook = Position(start_position.row,7), Position(start_position.row, 5)
        else: 
            start_position_of_rook, end_position_of_rook = Position(start_position.row,0), Position(start_position.row, 3)  
        
        self.board.move_piece(start_position_of_rook, end_position_of_rook) 


    def reset(self):
        self.__init__()
        
       
def is_castling_move(start_position: Position, end_position: Position):
    return abs(start_position.col - end_position.col) == 2



        

