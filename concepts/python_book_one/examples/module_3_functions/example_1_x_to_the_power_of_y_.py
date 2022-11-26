def handle_exceptions(
    base: int | float, exponent: int
) -> int | ValueError | dict[str, bool | int]:
    if not isinstance(base, (int, float)):
        raise ValueError("base needs to be an integer or float.")

    if exponent < 0:
        raise ValueError("exponent needs to be an integer greater or equal to zero.")

    if exponent == 0:
        return {"with_value_success": 1}

    return {"with_value_success": False}


def potencial(base: int | float, exponent: int = 0) -> int | float | ValueError:
    are_values_valid = handle_exceptions(base, exponent)

    if are_values_valid["with_value_success"]:
        return are_values_valid["with_value_success"]

    result = 1

    while exponent != 0:
        result = result * base

        exponent = exponent - 1

    return result


def first_alternative_potential_algorithm(
    base: int | float, exponent: int = 0
) -> int | float | ValueError:
    are_values_valid = handle_exceptions(base, exponent)

    if are_values_valid["with_value_success"]:
        return are_values_valid["with_value_success"]

    return base**exponent


def second_alternative_potential_algorithm(
    base: int | float, exponent: int = 0
) -> int | float | ValueError:
    are_values_valid = handle_exceptions(base, exponent)

    if are_values_valid["with_value_success"]:
        return are_values_valid["with_value_success"]

    return pow(base, exponent)
