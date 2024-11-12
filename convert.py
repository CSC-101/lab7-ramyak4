from typing import Optional

# Task 1
# This functions converts a given sting to a float value
# input: a string variable
# output: option of a float or None variable
def str_to_float(word: str) -> Optional[float]:
    try:
        return float(word)
    except ValueError:
        return None