# src/main.py
import pygame
import sys
import os 
from core.board import Board

def main():
    pygame.init()
    ROWS, COLS, SQUARE_SIZE = 8, 8, 60
    screen = pygame.display.set_mode((COLS * SQUARE_SIZE, ROWS * SQUARE_SIZE))
    pygame.display.set_caption("SpACH")

    board = Board(ROWS, COLS, SQUARE_SIZE)  # Crear instancia del tablero

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        board.draw_board(screen)  # Dibujar tablero
        pygame.display.flip()

    pygame.quit()
    print("El programa ha finalizado correctamente.")
    sys.exit()

if __name__ == "__main__":
    main()