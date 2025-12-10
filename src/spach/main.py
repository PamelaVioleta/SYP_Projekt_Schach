# src/spach/main.py
from core.board import Board
from core.pieces import Piece
def main():
    print("¡Bienvenida a SYP_Projekt_Schach, Pamela , Pal!")

    # Create the board
    chess_board = Board()

    # Create pieces black
    rook_black_1 = Piece("Rook", "black", (0,0)) 
    knight_black_1 = Piece("Knight", "black", (0,1))
    bischop_black_1 = Piece("Bischop", "black", (0, 2))
    queen_black = Piece("Queen", "black", (0, 3))
    king_black = Piece("King", "black", (0, 4))
    bischop_black_2 = Piece("Bischop", "black", (0, 5))
    knight_black_2 = Piece("knight","black",(0, 6))
    rook_black_2 = Piece("Rook", "black", (0, 7))
    pawn_black_0 = Piece("Pawn", "black", (1,0))
    pawn_black_1 = Piece("Pawn", "black", (1,1))
    pawn_black_2 = Piece("Pawn", "black", (1,2))
    pawn_black_3 = Piece("Pawn", "black", (1,3))
    pawn_black_4 = Piece("Pawn", "black", (1,4))
    pawn_black_5 = Piece("Pawn", "black", (1,5))
    pawn_black_6 = Piece("Pawn", "black", (1,6))
    pawn_black_7 = Piece("Pawn", "black", (1,7))
    
    # create piece white
    rook_white_1 = Piece("Rook", "white", (7,0)) 
    knight_white_1 = Piece("Knight", "white", (7,1))
    bischop_white_1 = Piece("Bischop", "white", (7, 2))
    queen_white = Piece("Queen", "white", (7, 3))
    king_white = Piece("King", "white", (7, 4))
    bischop_white_2 = Piece("Bischop", "white", (7, 5))
    knight_white_2 = Piece("knight","white",(7, 6))
    rook_white_2 = Piece("Rook", "white", (7, 7))
    pawn_white_0 = Piece("Pawn", "white", (6,0))
    pawn_white_1 = Piece("Pawn", "white", (6,1))
    pawn_white_2 = Piece("Pawn", "white", (6,2))
    pawn_white_3 = Piece("Pawn", "white", (6,3))
    pawn_white_4 = Piece("Pawn", "white", (6,4))
    pawn_white_5 = Piece("Pawn", "white", (6,5))
    pawn_white_6 = Piece("Pawn", "white", (6,6))
    pawn_white_7 = Piece("Pawn", "white", (6,7))


    # Place black_piece in the board
    chess_board.board[0][0] = rook_black_1
    chess_board.board[0][1] = knight_black_1
    chess_board.board[0][2] = bischop_black_1
    chess_board.board[0][3] = queen_black
    chess_board.board[0][4] = king_black
    chess_board.board[0][5] = bischop_black_2
    chess_board.board[0][6] = knight_black_2
    chess_board.board[0][7] = rook_black_2
    chess_board.board[1][0] = pawn_black_0
    chess_board.board[1][1] = pawn_black_1
    chess_board.board[1][2] = pawn_black_2
    chess_board.board[1][3] = pawn_black_3
    chess_board.board[1][4] = pawn_black_4
    chess_board.board[1][5] = pawn_black_5
    chess_board.board[1][6] = pawn_black_6
    chess_board.board[1][7] = pawn_black_7

    # Place white_pice in the board
    
    chess_board.board[7][0] = rook_white_1
    chess_board.board[7][1] = knight_white_1
    chess_board.board[7][2] = bischop_white_1
    chess_board.board[7][3] = queen_white
    chess_board.board[7][4] = king_white
    chess_board.board[7][5] = bischop_white_2
    chess_board.board[7][6] = knight_white_2
    chess_board.board[7][7] = rook_white_2
    chess_board.board[6][0] = pawn_white_0
    chess_board.board[6][1] = pawn_white_1
    chess_board.board[6][2] = pawn_white_2
    chess_board.board[6][3] = pawn_white_3
    chess_board.board[6][4] = pawn_white_4
    chess_board.board[6][5] = pawn_white_5
    chess_board.board[6][6] = pawn_white_6
    chess_board.board[6][7] = pawn_white_7


    # Print the board to console
    chess_board.print_board()

   # Try a valid move: pawn from (6,0) to (5,0)
    chess_board.move_piece((6, 0),(5, 0))
    chess_board.move_piece((6, 1),(4, 1))
    chess_board.move_piece((4, 1),(3, 1))
     # Try an invalid move: pawn from (5,0) to (5,1)
    chess_board.move_piece((5, 0),(5, 1))
    chess_board.move_piece((4, 1),(2, 1))
    


    #Print the board after the move
    print("\nBoard after move:")
    chess_board.print_board()
if __name__ == "__main__":
    main()
