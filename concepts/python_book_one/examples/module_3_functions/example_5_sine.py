DELTA = 0.000000000001


def signal_value(iterations: int) -> int:
    return 1 if iterations % 2 == 0 else -1


def term_formule(
    x_value: int | float, iterations: int, previous_term: int | float
) -> int | float:
    return -(
        (previous_term * x_value * x_value) / ((2 * iterations + 1) * 2 * iterations)
    )


def calculates_term(
    x_value: int | float, number_of_iterations: int, previous_term: int | float
) -> int | float:
    term = term_formule(x_value, number_of_iterations, previous_term)

    return term


def is_valid_approximated_value(x_value: int | float, delta: float = DELTA) -> bool:
    return abs(x_value) < delta


def sine(value: int | float) -> int | float:
    number_of_iterations = 0
    previous_term = value
    result = previous_term

    while not is_valid_approximated_value(previous_term):
        number_of_iterations = number_of_iterations + 1
        term = calculates_term(value, number_of_iterations, previous_term)
        result = result + term
        previous_term = term

    return result
