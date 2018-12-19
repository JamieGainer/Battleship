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

        self.squares = {}
        for board in ['human', 'computer']:
            self.squares[board] = {}
            self.squares[board] = {
                                  'ship_squares': {}.
                                  'sunk_ship_squares': {},
                                  'hits': set([]),
                                  'misses': set([])
                                  }


    def print_board(self, board):
        if board not in ['human', 'computer']:
            raise ValueError('Unknown option for board.')
        is_human = (board == human)
        for i in range(self.board_height):
            for j in range(self.board_width):
                if (i,j) in self.squares[board]['hits']:
                    print(' X ', end = '|')
                elif (i,j) in self.squares[board]['misses']:
                    print(' O ', end = '|')
                elif (i,j) in self.squares[board]['sunk_ship_squares']:
                    length = self.squares[board]['sunk_ship_squares'][(i,j)]
                    print(' ' + str(length), end = ' |')
                elif (i,j) in self.squares[board]['ship_squares'] and board == 
                    
                else:
                    print(' - ', end = '|')
            print()



    def setup_computer_ships(self, maxtries = 10000):
        self.computer_ship_squares = set([])
        self.computer_squares_by_ship = {}
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
                    self.computer_ship_squares.update(ship_squares)
                    self.computer_squares_by_ship[ship] = ship_squares
            if tries >= maxtries:
                raise RuntimeError("Unable to setup pieces")

