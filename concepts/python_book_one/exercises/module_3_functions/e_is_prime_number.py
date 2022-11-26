def is_prime_number(value: int) -> bool:
    from math import sqrt

    if not isinstance(value, int):
        raise ValueError("value needs to be an integer")

    if value < 2:
        return False

    result = True
    counter = 2

    while counter <= int(sqrt(value)):
        if value % counter == 0:
            result = False
            break
        else:
            counter = counter + 1

    return result
