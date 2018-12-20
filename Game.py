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
        assert self.board_width < 17 # so as not to reuse 'Q'
        self.ship_dict = default_ship_dict

        self.squares = {}
        for board in ['human', 'computer']:
            self.squares[board] = {
                                  'ship_squares': {},
                                  'sunk_ship_squares': {},
                                  'hits': set([]),
                                  'misses': set([])
                                  }
        self.ships = {'human': {}, 'computer': {}}
        self.sunk = {'human': [], 'computer': []}
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
                    length = self.squares[board]['sunk_ship_squares'][(i,j)]
                    print(' ' + str(length), end = ' |')
                elif (i,j) in self.squares[board]['ship_squares'] and is_human:
                    print(' $ ', end = '|')
                else:
                    print(' - ', end = '|')
            print()


    def setup_computer_ships(self, maxtries = 100000):
        ship_square_dict = self.squares['computer']['ship_squares']
        for ship, length in self.ship_dict.items():
            tries = 0
            while tries < maxtries: # Try to place success until successful
                ship_squares = set([])
                if random.random() > 0.5: # horizontal placement
                    TL_x = random.randint(0, self.board_width - length)
                    TL_y = random.randint(0, self.board_height - 1)
                    squares = [(x, TL_y) for x in range(TL_x, TL_x + length)]
                else:
                    TL_x = random.randint(0, self.board_width - 1)
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
                        self.ships['computer'][ship] = (set(ship_squares), set([]))
                    break
            if tries >= maxtries:
                raise RuntimeError("Unable to setup pieces")


    def setup_human_ships(self):
        import string
        for ship, length in self.ship_dict.items():
            while True:
                print("Please enter top left corner for", ship)
                print("(E.g. C6 gives 3rd column from left and 6th row from top.)")
                print("Or press 'q' or 'Q' to quit.")
                square = input()
                if square.upper() == 'Q':
                    return
                try:
                    column = string.ascii_uppercase.index(square[0].upper())
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
                    if square in self.squares['human']['ship_squares']:
                        print('Ship in the way!')
                        break
                else:
                    for square in squares:
                        self.squares['human']['ship_squares'][square] = (ship, length)
                        self.ships['human'][ship] = (set(squares), set([]))
                    break


    def computer_fires(self):
        import string
        while True:
            row = random.randint(0, self.board_height - 1)
            column = random.randint(0, self.board_width - 1)
            square = (row, column)
            for dict_name in ['hits', 'misses', 'sunk_ship_squares']:
                if square in self.squares['human'][dict_name]:
                    break
            else:
                print('Computer fires at', string.ascii_uppercase[column] + 
                      str(row + 1))
                if square in self.squares['human']['ship_squares']:
                    print('Hit!')
                    self.squares['human']['hits'].add(square)
                    for ship in self.ships['human']:
                        length = self.ship_dict[ship]
                        if square in self.ships['human'][ship][0]:
                            self.ships['human'][ship][0].remove(square)
                            self.ships['human'][ship][1].add(square)
                            if len(self.ships['human'][ship][0]) == 0: # sink
                                print('Computer sinks', ship, '\b!')
                                for square in self.ships['human'][ship][1]:
                                    self.squares['human']['hits'].remove(square)
                                    self.squares['human']['sunk_ship_squares'][square] = length
                                self.sunk['human'].append(ship)
                                if len(self.sunk['human']) == len(self.ship_dict):
                                    print('Game over!  Computer wins!')
                                    print('Human')
                                    self.print_board('human')
                                    print('Computer')
                                    self.print_board('computer')
                                    return "Game over"
                else:
                    print('Miss!')
                    self.squares['human']['misses'].add(square)
                break


    def play(self):
        import string
        self.setup_computer_ships()
        self.setup_human_ships()
        while True:
            print('What would you like to do?')
            print('[F]ire, [S]ee board, or [Q]uit?')
            answer = input()
            if answer.upper() not in ['F', 'Q', 'S']:
                print('Not sure what to do with that.')
                continue
            elif answer.upper() == 'Q':
                print('Bye')
                return
            elif answer.upper() == 'S':
                print('See [H]uman or [C]omputer board?')
                answer = input()
                if answer.upper() not in ['H', 'C']:
                    print('Not sure what to do with that.')
                    continue
                elif answer.upper() == 'H':
                    board = 'human'
                else:
                    board = 'computer'
                self.print_board(board)
            else:
                print("Please enter square to fire on.")
                print("(E.g. C6 gives 3rd column from left and 6th row from top.)")
                print("Or press 'q' or 'Q' to quit.")
                square_name = input()
                if square_name.upper() == 'Q':
                    return
                try:
                    column = string.ascii_uppercase.index(square_name[0].upper())
                    assert column >= 0 and column < self.board_width
                    row = int(square_name[1:]) - 1
                    assert row >= 0 and row < self.board_height
                    square = (row, column)
                except:
                    print('Invalid Square')
                    continue
                for dict_name in ['hits', 'misses', 'sunk_ship_squares']:
                    if square in self.squares['computer'][dict_name]:
                        print(square_name, 'already selected')
                        break
                else:
                    if square in self.squares['computer']['ship_squares']:
                        print('Hit!')
                        self.squares['computer']['hits'].add(square)
                        for ship in self.ships['computer']:
                            length = self.ship_dict[ship]
                            if square in self.ships['computer'][ship][0]:
                                self.ships['computer'][ship][0].remove(square)
                                self.ships['computer'][ship][1].add(square)
                                if len(self.ships['computer'][ship][0]) == 0: # sink
                                    print('Human sinks', ship, '\b!')
                                    for square in self.ships['computer'][ship][1]:
                                        self.squares['computer']['hits'].remove(square)
                                        self.squares['computer']['sunk_ship_squares'][square] = length
                                    self.sunk['computer'].append(ship)
                                    if len(self.sunk['computer']) == len(self.ship_dict):
                                        print('Game over!  Human wins!')
                                        print('Human')
                                        self.print_board('human')
                                        print('Computer')
                                        self.print_board('computer')
                                        return
                    else:
                        print('Miss!')
                        self.squares['computer']['misses'].add(square)
                    message = self.computer_fires()
                    if message == 'Game over':
                        return





