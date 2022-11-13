def calculate_entire_board_values(size: int = 64) -> list[int]:
    counter: int = 1
    result: list[int] = []

    for _ in range(0, size):
        result.append(counter)

        counter *= 2

    return result


def square(number: int) -> int | ValueError:
    if not isinstance(number, int) | 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")

    board_squares_values = calculate_entire_board_values()

    return board_squares_values[number - 1]


def total() -> int:
    result = sum(calculate_entire_board_values())

    return result
