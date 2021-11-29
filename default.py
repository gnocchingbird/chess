from piece import Piece, Piece_type

default_board = [
    [Piece(Piece_type.Rook, color="black"), Piece(Piece_type.Knight, color="black"), Piece(Piece_type.Bishop, color="black"), Piece(Piece_type.King, color="black"), Piece(Piece_type.Queen, color="black"), Piece(Piece_type.Bishop, color="black"), Piece(Piece_type.Knight, color="black"), Piece(Piece_type.Rook, color="black")],
    [Piece(Piece_type.Pawn, color="black"), Piece(Piece_type.Pawn, color="black"), Piece(Piece_type.Pawn, color="black"), Piece(Piece_type.Pawn, color="black"), Piece(Piece_type.Pawn, color="black"), Piece(Piece_type.Pawn, color="black"), Piece(Piece_type.Pawn, color="black"), Piece(Piece_type.Pawn, color="black")],
    [Piece(Piece_type.Empty), Piece(Piece_type.Empty), Piece(Piece_type.Empty), Piece(Piece_type.Empty), Piece(Piece_type.Empty), Piece(Piece_type.Empty), Piece(Piece_type.Empty), Piece(Piece_type.Empty)],
    [Piece(Piece_type.Empty), Piece(Piece_type.Empty), Piece(Piece_type.Empty), Piece(Piece_type.Empty), Piece(Piece_type.Empty), Piece(Piece_type.Empty), Piece(Piece_type.Empty), Piece(Piece_type.Empty)],
    [Piece(Piece_type.Empty), Piece(Piece_type.Empty), Piece(Piece_type.Empty), Piece(Piece_type.Empty), Piece(Piece_type.Empty), Piece(Piece_type.Empty), Piece(Piece_type.Empty), Piece(Piece_type.Empty)],
    [Piece(Piece_type.Empty), Piece(Piece_type.Empty), Piece(Piece_type.Empty), Piece(Piece_type.Empty), Piece(Piece_type.Empty), Piece(Piece_type.Empty), Piece(Piece_type.Empty), Piece(Piece_type.Empty)],
    [Piece(Piece_type.Pawn, color="white"), Piece(Piece_type.Pawn, color="white"), Piece(Piece_type.Pawn, color="white"), Piece(Piece_type.Pawn, color="white"), Piece(Piece_type.Pawn, color="white"), Piece(Piece_type.Pawn, color="white"), Piece(Piece_type.Pawn, color="white"), Piece(Piece_type.Pawn, color="white")],
    [Piece(Piece_type.Rook, color="white"), Piece(Piece_type.Knight, color="white"), Piece(Piece_type.Bishop, color="white"), Piece(Piece_type.Queen, color="white"), Piece(Piece_type.King, color="white"), Piece(Piece_type.Bishop, color="white"), Piece(Piece_type.Knight, color="white"), Piece(Piece_type.Rook, color="white")],
]