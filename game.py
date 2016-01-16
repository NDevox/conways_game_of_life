class Game():
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = [['.' for _ in range(self.cols)] for _ in range(self.rows)]

    def start(self, *args):
        for row, col in args:
            self.board[row][col] = 'o'

    def alive_next(self, cell_row, cell_col):
        neighbours = ((-1, -1), (-1, 0), (-1, 1),
                      (0, -1), (0, 1),
                      (1, -1), (1, 0), (1, 1))
        count = 0
        for nrow, ncol in neighbours:
            try:
                if self.board[cell_row + nrow][cell_col + ncol] == 'o':
                    count += 1
            except IndexError:
                continue
            if count > 3:
                return '.'

        if count == 3 or (count == 2 and self.board[cell_row][cell_col] == 'o'):
            return 'o'
        else:
            return '.'

    def __next__(self):
        new_board = [[self.alive_next(cell_row, cell_col) for cell_col
                      in range(self.cols)] for cell_row
                     in range(self.rows)]

        self.board = new_board

    def __str__(self):
        screen = ''
        for row in self.board:
            for col in row:
                screen += ' ' + col
            screen += '\n'
        return screen

glider = ((1,2),(2,3),(3,1),(3,2),(3,3))

def glider_example():
    """
    Basic example of a glider on a 10 by 10 grid
    """
    import time

    ex = Game(10,10)
    ex.start(*glider)

    for _ in range(25):
        print(ex)
        time.sleep(0.5)
        ex.__next__()
