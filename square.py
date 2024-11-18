from piece import Piece
from position import Position


class Square:
    
    def __init__(self, position: Position, piece : Piece = None):
        self.position = position
        self.piece = piece


    def has_piece(self):
        return self.piece != None
    
    def has_rival_piece(self,is_white):
        return self.has_piece() and self.piece.is_white != is_white
    

    def has_team_piece(self, is_white):
        return self.has_piece() and self.piece.is_white == is_white
    
    
    

