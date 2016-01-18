class Game():
    """
    Game object.

    This holds all the methods required to create and run the game.

    We use o for alive and . for dead for reasons of aesthetics.

    Might move this into a GUI later, maybe tkinter, probably pygame. When this happens I'll probably switch o and . for
    True and False.
    """

    def __init__(self, rows=10, cols=10):
        """
        Initialiser creates a blank board.

        :param rows: int, number of grid rows
        :param cols: int, number of grid columns
        """
        self.rows = rows
        self.cols = cols
        self.board = [['.' for _ in range(self.cols)] for _ in range(self.rows)]

    def start(self, *args):
        """
        Assigns a starting shape onto the board.

        Note: this will not blank the board, it will only place the given co-ordinates on the board as alive.

        :param args: list of tuples, co-ordinates to be placed on the board.
        """
        for row, col in args:
            self.board[row][col] = 'o'

    def alive_next(self, cell_row, cell_col):
        """
        Takes the a current cell and finds it's neighbours. Then calculates how many neighbours are dead or alive.

        If neighbour doesn't exist (i.e. it's edge of board) then assumes that neighbour is dead.

        :param cell_row: int, current cells row
        :param cell_col: int, current cells column
        :return: str, either o or . depending on aliveness.
        """
        neighbours = ((-1, -1), (-1, 0), (-1, 1),
                      (0, -1), (0, 1),
                      (1, -1), (1, 0), (1, 1))
        count = 0
        for nrow, ncol in neighbours:
            try:
                if self.board[cell_row + nrow][cell_col + ncol] == 'o':
                    count += 1
            except IndexError:
                # We are at the edge of the board, assume neighbouring cell is dead.
                continue
            if count > 3:
                # Already past 3 so will always be dead, let's save a bit of time.
                return '.'

        if count == 3 or (count == 2 and self.board[cell_row][cell_col] == 'o'):
            return 'o'
        else:
            return '.'

    def __next__(self):
        """
        Calculates the next state of the board and assigns it.
        """
        self.board = [[self.alive_next(cell_row, cell_col) for cell_col
                      in range(self.cols)] for cell_row
                     in range(self.rows)]

    def __str__(self):
        """
        Prints the board to screen
        """
        screen = ''
        for row in self.board:
            for col in row:
                screen += ' ' + col
            screen += '\n'
        return screen


def glider_example():
    """
    Basic example of a glider on a 10 by 10 grid
    """
    import time

    glider = ((1,2),(2,3),(3,1),(3,2),(3,3))

    ex = Game(10,10)
    ex.start(*glider)

    for _ in range(25):
        print(ex)
        time.sleep(0.5)
        ex.__next__()
