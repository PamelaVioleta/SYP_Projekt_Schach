# src/spach/core/board.py
class Board:
    def __init__(self):
        #Create a empty 8x8 board using two regular for loops
        self.board = []
        for i in range(8):
            fila = []
            for j in range(8):
                fila.append(None)
            self.board.append(fila)
    
    def print_board(self):
        print("Chessboard")
        for row in self.board:
            print(row)

    def is_valid_move(self, piece, start, end):
        """
        check if a move is valit for a given piece.
        Parameters
            piece: Piece 
                The chess piece to move.
            start: tuple
                Starting coordinates(row, col).
            end: tuple
                Traget coordinates (row, col).
        Returns
        bool
            True if the move is valid, False otherwise
        """
        if piece is None:
            print(f"No piece at position {start}")
            return False
            # Only work with the white pawn.
        elif piece.name == "Pawn" and piece.color == "white":
            start_row, start_col = start
            end_row, end_col = end
            # Only one move forward.
            if end_row == start_row -1 and end_col == start_col: 
                if self.board[end_row][end_col] is None:
                    return True
                else: 
                    return False
            # Two moves forward.
            elif start_row == 6 and start_col == end_col:
                if self.board[start_row -1][start_col] is None and self.board[start_row -2][start_col] is None:
                    return True
                else:
                    return False
            else:
                return False

        return False


    def move_piece(self, start, end):
        """
        Move a piece from start to end coordinates.

        start: tuple (row, col)
        end: tuple (row, col)
        """
        #start[0] always points to the first element of the tuple your passed(the row)
        #start[1] always points to the second element of the tuple(the column) 
        piece = self.board[start[0]][start[1]]
        if self.is_valid_move(piece, start, end):
            # Move the piece
            self.board[end[0]][end[1]] = piece # Place piece in the new position
            self.board[start[0]][start[1]]= None #Clear the old position
            piece.position = end               #update internal piece position          
            print("Move valid")
            print(f"Moved {piece} from {start} to {end}")
        else:
            print("Move invalid!")
            print(f"No moved {piece} from {start} to {end}")
            
        