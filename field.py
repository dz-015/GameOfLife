"""field module"""

from cell import Cell

from itertools import product
from typing import List, Iterator
from random import choice, seed
from time import time
from copy import deepcopy


class Field:
    def __init__(self, rows: int, cols: int, randomize: bool = True) -> None:
        self.__rows_num: int = rows
        self.__cols_num: int = cols
        self.__field: List[List[Cell]] = []

        if randomize:
            self.randomize()

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> Iterator:
        previous_state = self.__field
        self.__field = self.next_state()
        return previous_state

    def randomize(self) -> None:
        seed(time)
        for _ in range(self.__rows_num):
            row: List[Cell] = []

            for _ in range(self.__cols_num):
                cell = Cell(choice((True, False)))
                row.append(cell)

            self.__field.append(row)

    def next_state(self) -> List[List[Cell]]:
        new_field = deepcopy(self.__field)

        for x in range(self.__rows_num):
            for y in range(self.__cols_num):
                neighbours = 0
                for offset_x, offset_y in product(range(-1, 2), range(-1, 2)):
                    if 0 <= x + offset_x < self.__rows_num and 0 <= y + offset_y < self.__cols_num:
                        neighbours += int(self.__field[x + offset_x][y + offset_y].get_value())

                neighbours -= int(self.__field[x][y].get_value())  # cell counts itself at some point

                if new_field[x][y]:
                    if not 2 <= neighbours <= 3:
                        new_field[x][y].set_value(False)
                else:
                    if neighbours == 3:
                        new_field[x][y].set_value(True)
        return new_field
