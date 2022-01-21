from piece import Piece, Piece_type

def can_move(board: list, piece: Piece, old_pos: tuple, new_pos: tuple):
    if piece.color == board[new_pos[1]][new_pos[0]].color:
        return False
    if old_pos == new_pos:
        return False

    def move_diff(pos0, pos):
        return (pos[0] - pos0[0], pos[1] - pos0[1])
    
    def abs_diff(pos0, pos):
        return (abs(pos[0] - pos0[0]), abs(pos[1] - pos0[1]))
        
    if piece.piece_type == Piece_type.Empty:
        return False

    if piece.piece_type == Piece_type.Pawn:
        allowed = []
        if piece.color == "white":
            allowed.append((0, -1))
            if piece.first_move:
                allowed.append((0, -2)) # first move
            if board[old_pos[1] - 1][old_pos[0] - 1].color == "black": # front left
                allowed.append((-1, -1)) # board flipped
            if board[old_pos[1] - 1][old_pos[0] + 1].color == "black": # front right
                allowed.append((1, -1))
            return True if move_diff(old_pos, new_pos) in allowed else False # kinda inefficient to re-fill allowed every time
        elif piece.color == "black":
            allowed.append((0, 1))
            if piece.first_move:
                allowed.append((0, 2))
            if board[old_pos[1] + 1][old_pos[0] - 1].color == "white":
                allowed.append((-1, 1))
            if board[old_pos[1] + 1][old_pos[0] + 1].color == "white":
                allowed.append((1, 1))
            return True if move_diff(old_pos, new_pos) in allowed else False
        else:
            return False

    if piece.piece_type == Piece_type.Knight:
        diff = abs_diff(old_pos, new_pos)
        return True if 3 not in diff and sum(diff) == 3 else False
    
    if piece.piece_type == Piece_type.Bishop:
        diff = abs_diff(old_pos, new_pos)
        return True if diff[0] == diff[1] else False

    if piece.piece_type == Piece_type.Rook:
        diff = move_diff(old_pos, new_pos)
#        temp = (0, 0)
#        if 0 == diff[0]:
#            if diff[1] > 0:
#                temp = (0, diff[1] - 1)
#            else:
#                temp = (0, diff[1] + 1)
#        elif 0 == diff[1]:
#            if diff[0] > 0:
#                temp = (diff[0] - 1, 0)
#            else:
#                temp = (diff[0] + 1, 0)
#
        return True if 0 in diff else False #and can_move(board, piece, old_pos, temp) else False

    if piece.piece_type == Piece_type.King:
        diff = abs_diff(old_pos, new_pos)
        return True if not False in map((lambda n: n <= 1), diff) else False

    if piece.piece_type == Piece_type.Queen:
        mdiff = move_diff(old_pos, new_pos)
        adiff = abs_diff(old_pos, new_pos)
        return True if adiff[0] == adiff[1] or 0 in mdiff else False

    else:
        return True

#(lambda pos: print(pos) abs(pos[0]) + abs(pos[1]))