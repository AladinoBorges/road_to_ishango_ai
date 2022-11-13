def is_armstrong_number(number: int) -> bool:
    if not isinstance(number, int):
        raise ValueError("number needs to be an integer")

    iterable_number = str(number)
    number_length = len(iterable_number)

    digits_powered_by_number_length = [
        pow(int(digit), number_length) for digit in iterable_number
    ]

    result = sum(digits_powered_by_number_length)

    return result == number
