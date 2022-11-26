def is_triangular(value: int) -> bool:
    if not isinstance(value, int):
        raise ValueError("value needs to be a positive integer.")

    if value == 0:
        return False

    counter = 0
    integer_counter = 1

    while counter <= value:
        counter = counter + integer_counter
        integer_counter = integer_counter + 1

        if counter == value:
            return True

    return False
