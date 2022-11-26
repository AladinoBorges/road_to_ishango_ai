def sum_power(r_value: int, n_value: int) -> ValueError | int:
    if not isinstance(n_value, int) or n_value < 0:
        raise ValueError("n value needs to be an positive integer.")

    result = 1
    counter = 1

    while counter < n_value + 1:
        result = result + (r_value**counter)
        counter = counter + 1

    return result


print(sum_power(2, 4))
