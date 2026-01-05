# src/core/board.py
import pygame

class Board:
    def __init__(self, rows, cols, square_size):
        self.rows = rows
        self.cols = cols
        self.square_size = square_size

        self.pieces = [
            ['♜','♞','♝','♛','♚','♝','♞','♜'],
            ['♟','♟','♟','♟','♟','♟','♟','♟'],
            ['','','','','','','',''],
            ['','','','','','','',''],
            ['','','','','','','',''],
            ['','','','','','','',''],
            ['♙','♙','♙','♙','♙','♙','♙','♙'],
            ['♖','♘','♗','♕','♔','♗','♘','♖']
        ]

    def draw_board(self, screen):
        LIGHT = (245, 245, 220)  # color claro
        DARK = (139, 69, 19)     # color oscuro

        font = pygame.font.SysFont("DejaVu Sans", 48)

        for row in range(self.rows):
            for col in range(self.cols):
                color = LIGHT if (row + col) % 2 == 0 else DARK
                x = col * self.square_size
                y = row * self.square_size
                pygame.draw.rect(screen, color, (x, y, self.square_size, self.square_size))

                piece = self.pieces[row][col]
                if piece != '':
                    text = font.render(piece, True, (0, 0, 0))
                    screen.blit(text, (x + 15, y + 10))