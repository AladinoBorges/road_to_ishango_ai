def number_of_factors(x_value: int) -> int:
    values = 0
    iteration = 1

    while iteration <= x_value:
        if x_value % iteration == 0:
            values = values + 1
            iteration = iteration + 1
        else:
            iteration = iteration + 1

    return values
