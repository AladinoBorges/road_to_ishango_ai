def square_of_sum(number: int) -> int:
    sum_result = sum(range(1, number + 1))
    total_squared = pow(sum_result, 2)

    return total_squared


def sum_of_squares(number: int) -> int:
    square_values = [pow(value, 2) for value in range(1, number + 1)]
    total = sum(square_values)

    return total


def difference_of_squares(number: int) -> int:
    if not isinstance(number, int) or number <= 0:
        raise ValueError("value needs to be a natural number")

    return square_of_sum(number) - sum_of_squares(number)
