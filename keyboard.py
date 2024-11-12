from convert import str_to_float


# Task 2
# This function
def gather_numbers() -> list[float]:
    nums = []
    while True:
        value = input("Enter a number")
        if value.lower() == 'done':
           break
        if str_to_float(value) is not None:
            nums.append(str_to_float(value))
    return nums

if __name__ == '__main__':
    print("Sum of numbers:", sum(gather_numbers()))