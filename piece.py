from abc import ABC, abstractmethod
from typing import List
from position import Position





class Piece(ABC):
    def __init__(self, is_white: bool, is_killed: bool, square):
        self.is_white = is_white
        self.is_killed = is_killed
        self.square = square


    @abstractmethod
    def get_valid_moves(self, board) -> List[Position]:
        pass



class Rook(Piece):

    def __init__(self, is_white, is_killed, square):
        super().__init__(is_white, is_killed, square)


    def get_valid_moves(self, board):
        valid_moves = []
        current_position = self.square.position

        #UP
        for x in range(current_position.x + 1, 8):
            square = board[x][current_position.y]

            if square.has_team_piece(self.is_white):
                break
            if square.has_rival_piece(self.is_white):
                valid_moves.append(square.position)  #valid_moves.append(square.position)
                break
           
            valid_moves.append(square.position)
        
        #Down
        for x in range(current_position.x -1, -1, -1):
            square = board[x][current_position.y]

            if square.has_team_piece(self.is_white):
                break
            if square.has_rival_piece(self.is_white):
                valid_moves.append(square.position)
                break
           
            valid_moves.append(square.position)

        #Right

        for y in range(current_position.y + 1, 8):
            square = board[current_position.x][y]

            if square.has_team_piece(self.is_white):
                break
            if square.has_rival_piece(self.is_white):
                valid_moves.append(square.position)
                break
           
            valid_moves.append(square.position)


        #Left

        for y in range(current_position.y - 1, -1, -1):
            square = board[current_position.x][y]

            if square.has_team_piece(self.is_white):
                break
            if square.has_rival_piece(self.is_white):
                valid_moves.append(square.position)
                break
           
            valid_moves.append(square.position)

        return valid_moves


    def __str__(self):
        return "R"


class Pawn(Piece):

    def __init__(self, is_white, is_killed, square, is_first_move):
        self.is_first_move = is_first_move
        super().__init__(is_white, is_killed, square)


    def get_valid_moves(self,  board):

        pass

    def __str__(self):
        return "P"


class Bishop(Piece):

    def __init__(self, is_white, is_killed, square):
        super().__init__(is_white, is_killed, square)


    def get_valid_moves(self,  board):
        valid_moves = []
        current_position = self.square.position
        
        #UP Right
        i, j = current_position.x + 1, current_position.y + 1
        while(i<8 and i>-1 and j<8 and j>-1):
            square = board[i][j]

            if square.has_team_piece(self.is_white):
                break
            if square.has_rival_piece(self.is_white):
                valid_moves.append(square.position)
                break
           
            valid_moves.append(square.position)

            i +=1
            j +=1

        #UP LEFT
        i, j = current_position.x - 1, current_position.y + 1
        while(i<8 and i>-1 and j<8 and j>-1):
            square = board[i][j]

            if square.has_team_piece(self.is_white):
                break
            if square.has_rival_piece(self.is_white):
                valid_moves.append(square.position)
                break
           
            valid_moves.append(square.position)

            i -=1
            j +=1

        #DOWN Right
        i, j = current_position.x + 1, current_position.y - 1
        while(i<8 and i>-1 and j<8 and j>-1):
            square = board[i][j]

            if square.has_team_piece(self.is_white):
                break
            if square.has_rival_piece(self.is_white):
                valid_moves.append(square.position)
                break
           
            valid_moves.append(square.position)

            i +=1
            j -=1
        
        #DOWN LEFT
        i, j = current_position.x - 1, current_position.y - 1
        while(i<8 and i>-1 and j<8 and j>-1):
            square = board[i][j]

            if square.has_team_piece(self.is_white):
                break
            if square.has_rival_piece(self.is_white):
                valid_moves.append(square.position)
                break
           
            valid_moves.append(square.position)

            i -=1
            j -=1

        return valid_moves

    def __str__(self):
        return "B"


class Knight(Piece):

    def __init__(self, is_white, is_killed, square):
        super().__init__(is_white, is_killed, square)


    def get_valid_moves(self,  board):
        valid_moves = []
        current_position = self.square.position
        possible_moves = [(current_position.x+1, current_position.y+2),
                          (current_position.x-1, current_position.y+2),
                          (current_position.x+1, current_position.y-2),
                          (current_position.x-1, current_position.y-2),
                          (current_position.x+2, current_position.y+1),
                          (current_position.x-2, current_position.y+1),
                          (current_position.x+2, current_position.y-1),
                          (current_position.x-2, current_position.y-1)]
        
        for possible_move in possible_moves:
            x,y = possible_move
            if x<8 and x>=0 and y>=0 and  y<8:
                square = board[x][y]
                if not square.has_team_piece(self.is_white):
                    valid_moves.append(square.position)


        return valid_moves

        



    def __str__(self):
        return "H"



class Queen(Piece):

    def __init__(self, is_white, is_killed, square):
        super().__init__(is_white, is_killed, square)


    def get_valid_moves(self,  board):
        pass

    def __str__(self):
     return "Q"


class King(Piece):

    def __init__(self, is_white, is_killed, square):
        super().__init__(is_white, is_killed, square)


    def get_valid_moves(self,  board):
        pass

    def __str__(self):
        return "K"


   


#the loops in bishop rooks and queen are redundant. how about create a method that loops in the direction of the increments
# given for i and j



    

