from position import Position
from square import Square
from piece import *

class Board:


    def __init__(self):
        self.squares = [[None for i in range(8)] for i in range(8)]
        self.setup_board()


    def setup_board(self):
        self.squares[0][0] = Square(Position(0, 0))
        self.squares[0][0].piece = Rook(False, False, self.squares[0][0])

        self.squares[0][1] = Square(Position(0, 1))
        self.squares[0][1].piece = Knight(False, False, self.squares[0][1])

        self.squares[0][2] = Square(Position(0, 2))
        self.squares[0][2].piece = Bishop(False, False, self.squares[0][2])

        self.squares[0][3] = Square(Position(0, 3))
        self.squares[0][3].piece = Queen(False, False, self.squares[0][3])

        self.squares[0][4] = Square(Position(0, 4))
        self.squares[0][4].piece = King(False, False, self.squares[0][4])

        self.squares[0][5] = Square(Position(0, 5))
        self.squares[0][5].piece = Bishop(False, False, self.squares[0][5])

        self.squares[0][6] = Square(Position(0, 6))
        self.squares[0][6].piece = Knight(False, False, self.squares[0][6])

        self.squares[0][7] = Square(Position(0, 7))
        self.squares[0][7].piece = Rook(False, False, self.squares[0][7])

        self.squares[7][0] = Square(Position(7, 0))
        self.squares[7][0].piece = Rook(True, False, self.squares[7][0])

        self.squares[7][1] = Square(Position(7, 1))
        self.squares[7][1].piece = Knight(True, False, self.squares[7][1])

        self.squares[7][2] = Square(Position(7, 2))
        self.squares[7][2].piece = Bishop(True, False, self.squares[7][2])

        self.squares[7][3] = Square(Position(7, 3))
        self.squares[7][3].piece = Queen(True, False, self.squares[7][3])

        self.squares[7][4] = Square(Position(7, 4))
        self.squares[7][4].piece = King(True, False, self.squares[7][4])

        self.squares[7][5] = Square(Position(7, 5))
        self.squares[7][5].piece = Bishop(True, False, self.squares[7][5])

        self.squares[7][6] = Square(Position(7, 6))
        self.squares[7][6].piece = Knight(True, False, self.squares[7][6])

        self.squares[7][7] = Square(Position(7, 7))
        self.squares[7][7].piece = Rook(True, False, self.squares[7][7])


        #place pawns
        for j in range(0,8):
            self.squares[1][j] = Square(Position(1,j))
            self.squares[1][j].piece = Pawn(False,False,self.squares[1][j])
            self.squares[6][j] = Square(Position(6,j))
            self.squares[6][j].piece = Pawn(True,False,self.squares[6][j])

        #place empty Squares
        for i in range (2,6):
            for j in range(0,8):
                self.squares[i][j] = Square(Position(i,j))


    def print_board(self):
        for i in range(0, len(self.squares)):
            print()
            for j in range(0, len(self.squares[i])):
                piece = self.squares[i][j].piece
                if piece != None:
                    print(piece, end= ' ')

                else:
                    print('-', end = ' ')

    
    def move_piece(self, start_position: Position, end_position: Position):
        start_square = self.squares[start_position.row][start_position.col]
        end_square = self.squares[end_position.row][end_position.col]

        end_square.piece = start_square.piece
        end_square.piece.square = end_square
        start_square.piece = None

    def undo_move(self, start_position: Position, end_position: Position, captured_piece = None):
        start_square = self.squares[start_position.row][start_position.col]
        end_square = self.squares[end_position.row][end_position.col]

        start_square.piece = end_square.piece
        if start_square.piece:
            start_square.piece.square = start_square
        
        end_square.piece = captured_piece

        if captured_piece:
            captured_piece.square = end_square

    

    
def is_castling_move(start_position: Position, end_position: Position):
    return abs(start_position.col - end_position.col) == 2




        
        


 