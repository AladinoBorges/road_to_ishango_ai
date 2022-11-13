def degenerate(sides: list[int]) -> bool:
    [a, b, c] = sides

    is_degenerate = a + b == c or a + c == b or b + c == a

    if is_degenerate:
        raise ValueError(
            "\nthe sum of the length of two sides equals that of of the third.\n"
            + "in that case, the triangle has a zero area and looks line a single line",
        )

    return False


def invalid_values(sides: list[int]) -> bool:
    [a, b, c] = sides

    is_invalid = 0 == a or 0 == b or 0 == c and sum(sides) == 0

    return is_invalid


def triangle_inequality(sides: list[int]) -> bool:
    [a, b, c] = sides

    is_valid = a + b >= c and a + c >= b and b + c >= a

    return is_valid


def validate_triangle(sides: list[int]) -> bool:
    if invalid_values(sides):
        return False

    if not triangle_inequality(sides):
        return False

    degenerate(sides)

    return True


def equilateral(sides: list[int]) -> bool:
    is_valid = validate_triangle(sides)

    if not is_valid:
        return False

    [a, b, c] = sides

    return a == b == c


def isosceles(sides: list[int]) -> bool:
    is_valid = validate_triangle(sides)

    if not is_valid:
        return False

    [a, b, c] = sides

    return a == b or b == c or a == c


def scalene(sides: list[int]) -> bool:
    is_valid = validate_triangle(sides)

    if not is_valid:
        return False

    [a, b, c] = sides

    return a != b and b != c and c != a
