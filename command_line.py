import sys
from typing import List
from convert import str_to_float

def sum_command_line_args(arguments: List[str]) -> float:
    total = 0.0
    for arg in arguments:
        value = str_to_float(arg)
        if value is not None:
            total += value
    return total

if __name__ == '__main__':
    print(sys.argv)

