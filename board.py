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
            self.squares[1][j].piece = Pawn(False,False,self.squares[1][j], True)
            self.squares[6][j] = Square(Position(6,j))
            self.squares[6][j].piece = Pawn(True,False,self.squares[6][j], True)

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


    def move_piece(self, start_position: Position, end_position: Position) -> bool:
        if (start_position.row >7 or start_position.row <0 or start_position.col > 7 
            or start_position.col<0 or end_position.row >7 or end_position.row <0 or end_position.col > 7 or end_position.col<0):
            return False
        
        start_square = self.squares[start_position.row][start_position.col]
        end_square = self.squares[end_position.row][end_position.col]
        piece = start_square.piece
        print(piece)

        if piece == None:
            print('Error: There is no piece in this square')
            return False
        
        valid_piece_moves = piece.get_valid_moves(self.squares)
        is_valid_move = any(position.row == end_position.row and position.col == end_position.col for position in valid_piece_moves)
        if is_valid_move:
            end_square.piece = piece
            end_square.piece.square = end_square
            start_square.piece = None
            if isinstance(end_square.piece, Pawn):
                end_square.piece.is_first_move = False
            return True
        else:
            print("Error: Cannot move to that square")
            return False
        

        


        
        


 