def factorial(value: int) -> int:
    result = 1

    while value != 0:
        result = result * value

        value = value - 1

    return result


def exponential_taylor_series(x_value: int, iterations: int = 10) -> float:
    """source explanation:
    https://pythonforundergradengineers.com/creating-taylor-series-functions-with-python.html
    """
    counter = 1
    result = 1

    while counter <= iterations:
        result = result + ((x_value**counter) / factorial(counter))
        counter = counter + 1

    return result
