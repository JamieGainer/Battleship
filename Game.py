""" Placeholder for docstring """

import random

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

    def setup_computer_ships(self, maxtries = 10000):
        computer_ship_squares = set([])
        squares_by_ship = {}
        for ship, length in self.ship_dict.items():
            tries = 0
            while tries < maxtries: # Try to place success until successful
                ship_squares = set([])
                if random.random > 0.5: # try horizontal placement
                    TL_x = random.randint(0, self.board_width - length)
                    TL_y = random.randint(0, self.board_height)
                    squares = [(x, TL_y) for x in range(TL_x, TL_x + length)]
                else:
                    TL_x = random.randint(0, self.board_width)
                    TL_y = random.randint(0, self.board_height - length)
                    squares = [(TL_x, y) for y in range(TL_y, TL_y + length)]
                for square in squares:
                    if square in computer_ship_squares:
                        tries += 1
                        break
                    else:
                        ship_squares.add(square)
                else:
                    computer_ship_squares.update(ship_squares)
                    squares_by_ship[ship] = ship_squares
            if tries >= maxtries:
                raise RuntimeError("Unable to setup pieces")

