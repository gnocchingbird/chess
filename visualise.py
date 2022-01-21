import pygame
from piece import Piece, Piece_type
from images import piece_images

def clear_board(window):
    window.fill((50, 35, 20))

    for row in range(8):
        for col in range(0, 8, 2):
            pygame.draw.rect(window, (255, 230, 200), [(col + row % 2) * 100, row * 100, 100, 100])
    
    #pygame.display.update()

def load_pieces() -> dict:
    return {p_type: pygame.image.load(img_path) for p_type, img_path in piece_images.items()}

def draw_pieces(window, board: list, images: dict):
    for y, row in enumerate(board):
        for x, piece in enumerate(row):
            if piece.is_empty():
                continue

            window.blit(images[piece.piece_type], (x * 100, y * 100))

    #pygame.display.update()

def highlight_field(window, board: list, piece: Piece, x: int, y: int, images: dict, color: tuple):
    pygame.draw.rect(window, color, [x * 100, y * 100, 100, 100])
    if not piece.piece_type == Piece_type.Empty:
        window.blit(images[piece.piece_type], (x * 100, y * 100))


    #pygame.display.update()

def highlight_matching(window, board: list, match_func, images: dict, color: tuple):
    for y, row in enumerate(board):
        for x, piece in enumerate(row):
            if match_func(piece, (x, y)):
                highlight_field(window, board, piece, x, y, images, color)

def color_black_white(window, board: list):
    for y, row in enumerate(board):
        for x, piece in enumerate(row):
            if piece.color == "white":
                s = pygame.Surface((100, 100)) # because draw() apparently doesn't support alpha ~ https://stackoverflow.com/questions/6339057/draw-a-transparent-rectangles-and-polygons-in-pygame
                s.set_alpha(40)
                s.fill((255, 255, 255))
                window.blit(s, (x * 100, y * 100))
            elif piece.color == "black":
                s = pygame.Surface((100, 100)) # because draw() apparently doesn't support alpha ~ https://stackoverflow.com/questions/6339057/draw-a-transparent-rectangles-and-polygons-in-pygame
                s.set_alpha(70)
                s.fill((0, 0, 0))
                window.blit(s, (x * 100, y * 100))

def log_board(board: list):
    for row in board:
        print(" ", end="")
        for field in row:
            print(f"{field} ", end="")
        print("\n", end="")
        

if __name__ == "__main__":
    print(load_pieces())