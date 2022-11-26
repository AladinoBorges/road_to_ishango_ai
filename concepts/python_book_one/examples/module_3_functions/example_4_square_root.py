DELTA = 0.000000000001


def square_root_guess_formula(x_value: int | float, guess: int | float) -> int | float:
    formula = (guess + x_value / guess) / 2

    return formula


def is_great_guess_based_on_limiar_error(
    value: int | float, guess: int | float, delta: float = DELTA
) -> bool:
    return abs((guess * guess) - value) < delta


def is_great_guess_based_on_relative_error(
    value: int | float, guess: int | float, delta: float = DELTA
) -> bool:
    return abs(((guess * guess) - value) / value) < delta


def next_guess(value: int | float, guess: int | float) -> int | float:
    result = square_root_guess_formula(value, guess)

    return result


def square_root(value: int | float, guess: int | float = 1) -> int | float:
    while not is_great_guess_based_on_limiar_error(value, guess):
        guess = next_guess(value, guess)

    return guess
