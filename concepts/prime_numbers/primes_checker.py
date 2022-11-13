def is_prime_number(number: int) -> bool:
    if number <= 1 or not isinstance(number, int):
        raise ValueError("number needs to be an integer greater than 1")

    is_prime = True

    for value in range(2, number):
        if number % value == 0:
            is_prime = False

            break

    return is_prime
