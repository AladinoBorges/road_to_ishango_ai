def factorial(value: int) -> int:
    if value < 2:
        return 1

    result = 1

    for value in range(2, value + 1):
        result *= value

    return result


def equation_of_x_and_n_values(x_value: int | float, n_limit: int) -> float:
    start_to_finish_values = [
        (pow(x_value, n_value) / factorial(n_value))
        for n_value in range(2, n_limit + 1)
    ]

    return start_to_finish_values


def calculate_sum() -> float:
    x_value = eval(input("insert the value of x:\n-> "))
    n_value = eval(input("insert the value of n:\n-> "))

    x_and_n_equation_result = equation_of_x_and_n_values(x_value, n_value)

    result = 1 + x_value + sum(x_and_n_equation_result)

    return f"the sum value is: {result}"
