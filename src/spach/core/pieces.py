# src/spach/core/pieces.py
class Piece:
    def __init__(self, name, color, position):
        """
        Initialize a chess piece.

        Parameters:
        name(str): Name of the piece, e.g. "Pawn", "Rook"
        Color(str): "while" or "black"
        position (tuple): Coordinates on the board as (row, column), e.g., (6,0)
        """
        self.name = name
        self.color = color
        self.position = position

    def __repr__(self):
        """
        Return a short representation for printing the board.
        Example: PW = white pawn, Rn = black rook
        """
        if self.name == "Knight":
            return f"{self.color[0].upper()}{self.name[1].upper()}" 
        else:
            return f"{self.color[0].upper()}{self.name[0].upper()}"  


    