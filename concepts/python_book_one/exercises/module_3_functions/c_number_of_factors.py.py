def number_of_factors(value: int) -> int:
    values = 0
    iteration = 1

    if not isinstance(value, int) or value < 0:
        raise ValueError("value needs to be an integer greater or equal to zero.")

    while iteration <= value:
        if value % iteration == 0:
            values = values + 1
            iteration = iteration + 1
        else:
            iteration = iteration + 1

    return values
