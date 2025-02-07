from tictactoe.src.models.cellStatus import CellStatus


class Cell:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.player = None
        self.status = CellStatus.EMPTY


    def print(self):
        if self.status == CellStatus.EMPTY:
            print("| |", end="")
        else:
            print(f" | {self.player.symbol.symbol} |", end="")