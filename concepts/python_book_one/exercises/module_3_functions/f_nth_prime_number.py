from e_is_prime_number import is_prime_number


def find_nth_prime(value: int) -> int:
    counter = 0
    nth_prime = 1

    while counter < value:
        if is_prime_number(nth_prime):
            counter = counter + 1

        nth_prime = nth_prime + 1

    return nth_prime - 1
