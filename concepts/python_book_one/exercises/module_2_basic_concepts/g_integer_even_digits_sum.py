def integer_even_digits_sum(number: int) -> str:
    digits = [int(value) for value in str(number) if int(value) % 2 == 0]

    return f"the sum of all even digits is: {sum(digits)}"
