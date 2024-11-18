from position import Position
from square import Square
from piece import *

class Board:


    def __init__(self):
        self.board = [[None for i in range(8)] for i in range(8)]
        self.setup_board()


    def setup_board(self):
        self.board[0][0] = Square(Position(0,0), Rook(True,False))
        self.board[0][1] = Square(Position(0,1), Knight(True,False))
        self.board[0][2] = Square(Position(0,2), Bishop(True,False))
        self.board[0][3] = Square(Position(0,3), Queen(True,False))
        self.board[0][4] = Square(Position(0,4), King(True,False))
        self.board[0][5] = Square(Position(0,5), Bishop(True,False))
        self.board[0][6] = Square(Position(0,6), Knight(True,False))
        self.board[0][7] = Square(Position(0,7), Rook(True,False))
        self.board[7][0] = Square(Position(7,0), Rook(False,True))
        self.board[7][1] = Square(Position(7,1), Knight(False,True))
        self.board[7][2] = Square(Position(7,2), Bishop(False,True))
        self.board[7][3] = Square(Position(7,3), Queen(False,True))
        self.board[7][4] = Square(Position(7,4), King(False,True))
        self.board[7][5] = Square(Position(7,5), Bishop(False,True))
        self.board[7][6] = Square(Position(7,6), Knight(False,True))
        self.board[7][7] = Square(Position(7,7), Rook(False,True))

        #place pawns
        for j in range(0,8):
            self.board[1][j] = Square(Position(1,j), Pawn(True,False))
            self.board[6][j] = Square(Position(6,j), Pawn(False,False))

        #place empty Squares
        for i in range (2,6):
            for j in range(0,8):
                self.board[i][j] = Square(Position(i,j))


    def print_board(self):
        for i in range(0, len(self.board)):
            print()
            for j in range(0, len(self.board[i])):
                piece = self.board[i][j].piece
                if piece != None:
                    print(piece, end= ' ')

                else:
                    print('-', end = ' ')

    






    
                

        




        
        return