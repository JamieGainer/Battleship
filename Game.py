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
        assert self.board_width < 26
        self.ship_dict = default_ship_dict

        self.squares = {}
        for board in ['human', 'computer']:
            self.squares[board] = {
                                  'ship_squares': {}.
                                  'sunk_ship_squares': {},
                                  'hits': set([]),
                                  'misses': set([])
                                  }
        self.ships = {'human': {}, 'computer': {}}
        self.ships_setup = False


    def print_board(self, board):
        if board not in ['human', 'computer']:
            raise ValueError('Unknown option for board.')
        is_human = (board == 'human')
        for i in range(self.board_height):
            for j in range(self.board_width):
                if (i,j) in self.squares[board]['hits']:
                    print(' X ', end = '|')
                elif (i,j) in self.squares[board]['misses']:
                    print(' O ', end = '|')
                elif (i,j) in self.squares[board]['sunk_ship_squares']:
                    length = self.squares[board]['sunk_ship_squares'][(i,j)][1]
                    print(' ' + str(length), end = ' |')
                elif (i,j) in self.squares[board]['ship_squares'] and is_human:
                    print(' = ', end = '|')
                else:
                    print(' - ', end = '|')
            print()


    def setup_computer_ships(self, maxtries = 10000):
        ship_square_dict = self.squares['computer']['ship_squares']
        for ship, length in self.ship_dict.items():
            ship_squares = set([])
            tries = 0
            while tries < maxtries: # Try to place success until successful
                if random.random > 0.5: # horizontal placement
                    TL_x = random.randint(0, self.board_width - length)
                    TL_y = random.randint(0, self.board_height)
                    squares = [(x, TL_y) for x in range(TL_x, TL_x + length)]
                else:
                    TL_x = random.randint(0, self.board_width)
                    TL_y = random.randint(0, self.board_height - length)
                    squares = [(TL_x, y) for y in range(TL_y, TL_y + length)]
                for square in squares:
                    if square in ship_square_dict:
                        tries += 1
                        break
                    else:
                        ship_squares.add(square)
                else:
                    for square in ship_squares:
                        ship_square_dict[square] = (ship, length)
            if tries >= maxtries:
                raise RuntimeError("Unable to setup pieces")


    def setup_human_ships(self):
        for ship, length in self.ship_dict.items():
            while True:
                print("Please enter top left corner for", ship)
                print("(E.g. C6 gives 3rd column from left and 6th row from top.)")
                print("Or press 'q' or 'Q' to quit.")
                square = input()
                if square.upper() == 'Q':
                    return
                try:
                    column = string.ascii_uppercase.index(square[0])
                    assert column >= 0 and column < self.board_width
                    row = int(square[1:]) - 1
                    assert row >= 0 and row < self.board_height
                except:
                    print('Invalid Square')
                    continue
                print("Please enter 'H' for horizontal or 'V' for vertical " + 
                      "placement of ship (or q/Q to quit).")
                orientation = input()
                if square.upper() == 'Q':
                    return
                try:
                    assert orientation.upper() in ['H', 'V']
                except:
                    print('Invalid Orientation')
                    continue
                if orientation.upper() == 'H':
                    squares = [(row, column + i) for i in range(length)]
                else:
                    squares = [(row + i, column) for i in range(length)]
                for square in squares:
                    if square in self.squares['human'].ship_squares:
                        print('Ship in the way!')
                        break
                else:
                    for square in squares:
                        self.squares['human'].ship_squares[square] = (ship, length)





