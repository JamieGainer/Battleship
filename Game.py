""" Placeholder for docstring """

default_ship_dict = {
                    'Carrier': 5,
                    'Battleship': 4,
                    'Cruiser': 3,
                    'Submarine': 3,
                    'Destroyer': 2
                     }

class Game():
"""Placeholder for docstring """

    def __init__(self, board_height = 10, board_width = 10, 
                 ship_dict = default_ship_dict):

        self.board_height = board_height
        self.board_width = board_width
        self.ship_dict = default_ship_dict

        self.human_sunk_ships = set([])
        self.computer_sunk_ships = set([])

        self.human_board = [[' O ' for j in range(self.board_width)]
                            for i in range(self.board.height)]
        self.computer_board = [[' O ' for j in range(self.board_width)]
                              for i in range(self.board.height)]

        self.human_plays = []
        self.computer_plays = []


    def print_board(self, board):
        for row in board:
            for space in row:
                print(space, end = '|')
            print()
