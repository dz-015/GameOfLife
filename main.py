from field import Field

from pprint import pprint
from time import sleep
import os


if os.name == 'nt':  # for windows
    def clear() -> None:
        os.system('cls')
else:  # for mac and linux aka posix
    def clear() -> None:
        os.system('clear')

if __name__ == '__main__':
    rows_num = int(input("Please enter a number of rows: "))
    cols_num = int(input("Now enter a number of columns: "))
    field = Field(rows_num, cols_num)

    for state in field:
        pprint(state)
        sleep(0.2)
        clear()
