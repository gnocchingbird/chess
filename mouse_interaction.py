from piece import Piece

def select_piece(board: list, pos: tuple) -> Piece:
    x, y = pos
    return board[y][x]

def move_piece(board: list, piece: Piece, old_pos: tuple, pos: tuple):
    old_x, old_y = old_pos
    x, y = pos
    board[old_y][old_x] = Piece()
    piece.first_move = False
    board[y][x] = piece