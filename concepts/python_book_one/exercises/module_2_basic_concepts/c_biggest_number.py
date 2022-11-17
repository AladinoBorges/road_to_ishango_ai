def biggest_number(range: int = 3) -> int | float | ValueError:
    numbers: list = []

    while len(numbers) < range:
        input_value = eval(
            input(f"{len(numbers) + 1}/{range} | insert one number:\n-> ")
        )

        if isinstance(input_value, int) or isinstance(input_value, float):
            numbers.append(input_value)

        else:
            raise ValueError("please, insert only numbers.")

    return max(numbers)
