def handle_exceptions(value: int) -> ValueError | dict[str, bool | int]:
    if not isinstance(value, (int)):
        raise ValueError("value needs to be an integer.")

    if value < 0:
        raise ValueError("value needs to be an integer greater or equal to zero.")

    if value == 0:
        return {"with_value_success": 1}

    return {"with_value_success": False}


def factorial(value: int) -> int | ValueError:
    is_value_valid = handle_exceptions(value)

    if is_value_valid["with_value_success"]:
        return is_value_valid["with_value_success"]

    result = 1

    while value != 0:
        result = result * value

        value = value - 1

    return result
