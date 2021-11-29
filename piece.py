import enum

class Piece_type(enum.Enum):
    Empty   = 0
    Pawn    = 1
    Knight  = 2
    Bishop  = 3
    Rook    = 4
    Queen   = 5
    King    = 6

colors = ("white", "black", "none")

class Piece(object):
    def __init__(self, pt: Piece_type = Piece_type.Empty, color: str = None):
        self.piece_type = pt
        self.color = color
    
    def __repr__(self):
        if self.piece_type == Piece_type.Empty:
            return "X"
        if self.piece_type == Piece_type.Pawn:
            return "P"
        if self.piece_type == Piece_type.Knight:
            return "K"
        if self.piece_type == Piece_type.Bishop:
            return "B"
        if self.piece_type == Piece_type.Rook:
            return "R"
        if self.piece_type == Piece_type.Queen:
            return "Q"
        if self.piece_type == Piece_type.King:
            return "O"
    
    def is_empty(self):
        return True if self.piece_type == Piece_type.Empty else False