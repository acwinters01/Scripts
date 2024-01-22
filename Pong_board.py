from turtle import Turtle

STARTING_POSITION = (0, 295)
NUM_OF_BOARD_PIECES = 18
SPACE_BETWEEN_PIECES = 30


class Board:

    def __init__(self):
        self.board_piece_positions = []
        self.place_board_piece()

    def board_pieces(self):
        new_y = STARTING_POSITION[1]
        for piece in range(NUM_OF_BOARD_PIECES):
            new_y -= SPACE_BETWEEN_PIECES
            position = (STARTING_POSITION[0], new_y)
            self.board_piece_positions.append(position)

    def place_board_piece(self):
        self.board_pieces()
        for position in self.board_piece_positions:
            board = Turtle("square")
            board.shapesize(stretch_len=.25, stretch_wid=.75)
            board.color("white")
            board.penup()
            board.goto(position)
