from abc import ABC, abstractmethod
from typing import List
from position import Position
from pathlib import Path




class Piece(ABC):
    def __init__(self, name: str, is_white: bool, is_killed: bool, square, image_path = None):
        self.name = name
        self.is_white = is_white
        self.is_killed = is_killed
        self.square = square
        self.image_path = image_path
        self.set_image()

    def set_image(self):
        color = 'white' if self.is_white else 'black'
        self.image_path = Path('assets')/'images'/'imgs-80px'/f'{color}_{self.name}.png'


    @abstractmethod
    def get_valid_moves(self, squares) -> List[Position]:
        pass



class Rook(Piece):

    def __init__(self, is_white, is_killed, square):
        super().__init__('rook',is_white, is_killed, square)


    def get_valid_moves(self, squares):
        valid_moves = []

        valid_moves_up = _loop_to_direction(1, 0, self.square, self.is_white, squares)
        valid_moves.extend(valid_moves_up)
        valid_moves_down = _loop_to_direction(-1, 0, self.square, self.is_white, squares)
        valid_moves.extend(valid_moves_down)
        valid_moves_right = _loop_to_direction(0, 1, self.square, self.is_white, squares)
        valid_moves.extend(valid_moves_right)
        valid_moves_left = _loop_to_direction(0, -1, self.square, self.is_white, squares)
        valid_moves.extend(valid_moves_left)

        return valid_moves


    def __str__(self):
        return "R"


class Pawn(Piece):

    def __init__(self, is_white, is_killed, square, is_first_move):
        self.is_first_move = is_first_move
        self.dir = -1 if is_white else 1
        super().__init__('pawn', is_white, is_killed, square)


    def get_valid_moves(self,  squares):
        #fix the moves of black pieces
        valid_moves = []
        current_position = self.square.position
        forward_moves = [(current_position.row + self.dir, current_position.col)]
        
        if self.is_first_move:
            forward_moves.append((current_position.row + 2*self.dir, current_position.col))
        
        capture_moves = [(current_position.row + self.dir, current_position.col+1),
                          (current_position.row + self.dir, current_position.col-1)]
        
        for row, col in forward_moves:
            if row<8 and row>=0 and col>=0 and col<8:
                square = squares[row][col]
                if square.has_piece():
                    break

                valid_moves.append(square.position)
   
        
        for row, col in capture_moves:
            if row<8 and row>=0 and col>=0 and col<8:
                square = squares[row][col]
                if square.has_rival_piece(self.is_white):
                    valid_moves.append(square.position)
            
        return valid_moves
        


    def __str__(self):
        return "P"


class Bishop(Piece):

    def __init__(self, is_white, is_killed, square):
        super().__init__('bishop', is_white, is_killed, square)


    def get_valid_moves(self,  squares):
        valid_moves = []

        valid_moves_up_right = _loop_to_direction(1, +1, self.square, self.is_white, squares)
        valid_moves.extend(valid_moves_up_right)
        valid_moves_up_left = _loop_to_direction(1, -1, self.square, self.is_white, squares)
        valid_moves.extend(valid_moves_up_left)
        valid_moves_down_right = _loop_to_direction(-1, 1, self.square, self.is_white, squares)
        valid_moves.extend(valid_moves_down_right)
        valid_moves_down_left = _loop_to_direction(-1,-1, self.square, self.is_white, squares)
        valid_moves.extend(valid_moves_down_left)

        return valid_moves

    
    def __str__(self):
        return "B"


class Knight(Piece):

    def __init__(self, is_white, is_killed, square):
        super().__init__('knight',is_white, is_killed, square)


    def get_valid_moves(self,  squares):
        valid_moves = []
        current_position = self.square.position
        possible_moves = [(current_position.row+1, current_position.col+2),
                          (current_position.row-1, current_position.col+2),
                          (current_position.row+1, current_position.col-2),
                          (current_position.row-1, current_position.col-2),
                          (current_position.row+2, current_position.col+1),
                          (current_position.row-2, current_position.col+1),
                          (current_position.row+2, current_position.col-1),
                          (current_position.row-2, current_position.col-1)]
        
        for possible_move in possible_moves:
            row, col = possible_move
            if row<8 and row>=0 and col>=0 and col<8:
                square = squares[row][col]
                if not square.has_team_piece(self.is_white):
                    valid_moves.append(square.position)


        return valid_moves

        



    def __str__(self):
        return "H"



class Queen(Piece):

    def __init__(self, is_white, is_killed, square):
        super().__init__('queen', is_white, is_killed, square)


    def get_valid_moves(self,  squares):
        valid_moves = []

        valid_moves_up = _loop_to_direction(1, 0, self.square, self.is_white, squares)
        valid_moves.extend(valid_moves_up)
        valid_moves_down = _loop_to_direction(-1, 0, self.square, self.is_white, squares)
        valid_moves.extend(valid_moves_down)
        valid_moves_right = _loop_to_direction(0, 1, self.square, self.is_white, squares)
        valid_moves.extend(valid_moves_right)
        valid_moves_left = _loop_to_direction(0, -1, self.square, self.is_white, squares)
        valid_moves.extend(valid_moves_left)
        valid_moves_up_right = _loop_to_direction(1, +1, self.square, self.is_white, squares)
        valid_moves.extend(valid_moves_up_right)
        valid_moves_up_left = _loop_to_direction(1, -1, self.square, self.is_white, squares)
        valid_moves.extend(valid_moves_up_left)
        valid_moves_down_right = _loop_to_direction(-1, 1, self.square, self.is_white, squares)
        valid_moves.extend(valid_moves_down_right)
        valid_moves_down_left = _loop_to_direction(-1,-1, self.square, self.is_white, squares)
        valid_moves.extend(valid_moves_down_left)

        return valid_moves
        

    def __str__(self):
     return "Q"


class King(Piece):

    def __init__(self, is_white, is_killed, square):
        super().__init__('king', is_white, is_killed, square)


    def get_valid_moves(self,  squares):
        valid_moves = []
        current_position = self.square.position
        possible_moves = [(current_position.row+1, current_position.col),
                          (current_position.row-1, current_position.col),
                          (current_position.row, current_position.col+1),
                          (current_position.row, current_position.col-1),
                          (current_position.row+1, current_position.col+1),
                          (current_position.row+1, current_position.col-1),
                          (current_position.row-1, current_position.col+1),
                          (current_position.row-1, current_position.col-1)]
        
        for possible_move in possible_moves:
            row, col = possible_move
            if row<8 and row>=0 and col>=0 and col<8:
                square = squares[row][col]
                if not square.has_team_piece(self.is_white):
                    valid_moves.append(square.position)

        return valid_moves
        

    def __str__(self):
        return "K"


#The loops in bishop rooks and queen are redundant. 
#This is a help method that loops in the direction of the row and column increments and gets the valid moves

def _loop_to_direction(row_incr, col_incr, current_square, is_white, squares) -> List[Position]:
    valid_moves = []   
    row = current_square.position.row + row_incr
    col = current_square.position.col + col_incr
    

    while(row<8 and row>=0 and col<8 and col>=0):
        square = squares[row][col]
        if square.has_team_piece(is_white):
            break
        if square.has_rival_piece(is_white):
            valid_moves.append(square.position)
            break
           
        valid_moves.append(square.position)

        row += row_incr
        col += col_incr

    return valid_moves

        



    

