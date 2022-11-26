def handle_exceptions(
    first_value: int, second_value: int
) -> ValueError | dict[str, bool | int]:
    if not isinstance(first_value, (int)) or not isinstance(second_value, (int)):
        raise ValueError("all values need to be integer.")

    if first_value < 0 or second_value < 0:
        raise ValueError("all values need to be an integer greater or equal to zero.")

    if second_value == 0:
        return {"with_value_success": first_value}

    return {"with_value_success": False}


def greatest_common_divisor(
    first_value: int, second_value: int = 0
) -> int | ValueError:
    are_values_valid = handle_exceptions(first_value, second_value)

    if are_values_valid["with_value_success"]:
        return are_values_valid["with_value_success"]

    result = None

    while second_value != 0:
        result = second_value

        second_value = first_value % second_value

    return result
