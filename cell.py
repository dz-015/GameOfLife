"""cell module"""


class Cell:
    def __init__(self, value: bool = False) -> None:
        self.__value: bool = value  # True if cell is alive

    def __bool__(self) -> bool:
        return self.__value

    def __repr__(self) -> str:
        return '■' if self else '□'

    def get_value(self) -> bool:
        return self.__value

    def set_value(self, value: bool) -> None:
        self.__value = value
