def inverter(value: str) -> str:
    return value[::-1]


def integer_inverter(number: int) -> str:
    result = inverter(str(number))

    return f"the inverted value or {number} is: {result}"
