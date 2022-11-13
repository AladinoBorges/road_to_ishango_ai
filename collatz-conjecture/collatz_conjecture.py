def odd_step(number: int) -> int:
    return (3 * number) + 1


def even_step(number: int) -> int:
    return int(number / 2)


def execute_correct_step(number: int) -> int:
    if number % 2 == 0:
        return even_step(number)

    return odd_step(number)


def steps(number: int, counter: int = 1) -> int | ValueError:
    if 1 > number or not isinstance(number, int):
        raise ValueError("Only positive integers are allowed")

    if number > 1:
        counter += 1

        step_value = execute_correct_step(number)

        return steps(step_value, counter)

    return counter - 1
