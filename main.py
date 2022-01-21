from logic import can_move
from piece import Piece, Piece_type
from visualise import clear_board, color_black_white, draw_pieces, highlight_field, highlight_matching, load_pieces, log_board
from default import default_board
from mouse_interaction import move_piece, select_piece
import pygame

board = default_board

def start_game():
    pygame.init()
    window = pygame.display.set_mode((len(board[0]) * 100, len(board) * 100))
    running = True
    mouse_free = True
    old_pos = (-1, -1)
    current_piece = None

    clear_board(window)
    images = load_pieces()
    draw_pieces(window, board, images)
    pygame.display.update()

    while running:
        for event in pygame.event.get(): # event-loop
            if event.type == pygame.QUIT:
                running = False
                pygame.display.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: # deselect piece if ESC is pressed
                    current_piece = None
                    mouse_free = True
                    clear_board(window)
                    draw_pieces(window, board, images)
                    pygame.display.update()
                elif event.key == pygame.K_SPACE: # color fields if Space is pressed
                    current_piece = None
                    mouse_free = True
                    clear_board(window)
                    color_black_white(window, board)
                    draw_pieces(window, board, images)
                    pygame.display.update()
                    print("space pressed")
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    current_piece = None
                    mouse_free = True
                    clear_board(window)
                    draw_pieces(window, board, images)
                    pygame.display.update()
                    print("space released")
            elif event.type == pygame.MOUSEBUTTONDOWN: # mouse-click
                mpos = pygame.mouse.get_pos()
                mpos = (mpos[0] // 100, mpos[1] // 100)
                if mouse_free: # first click
                    current_piece = select_piece(board, mpos)
                    if current_piece.piece_type != Piece_type.Empty: # only act on clicks on occupied fields
                        highlight_matching(window, board, (lambda p, pos: can_move(board, current_piece, mpos, pos)), images, (80, 10, 0))
                        highlight_field(window, board, current_piece, mpos[0], mpos[1], images, (20, 150, 0))
                        pygame.display.update()
                        old_pos = mpos # save to overwrite free space later
                        mouse_free = False
                    else:
                        current_piece = None
                else: #second click
                    if(can_move(board, current_piece, old_pos, mpos)):
                        move_piece(board, current_piece, old_pos, mpos)
                        clear_board(window)
                        draw_pieces(window, board, images)
                        pygame.display.update()
                        mouse_free = True
                        current_piece = None
                    






if __name__ == "__main__":
    start_game()