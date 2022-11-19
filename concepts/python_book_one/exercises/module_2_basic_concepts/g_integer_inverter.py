def inverter(value: str) -> str:
    return value[::-1]


def integer_inverter(number: int) -> int:
    result = inverter(str(number))

    return f"the inverted value or {number} is: {result}"
