def greater_whole_number() -> str:
    limit = eval(input("insert a limit (integer):\n-> "))

    counter = 0
    greater_integer = 0

    while greater_integer < limit:
        counter = counter + 1
        greater_integer = greater_integer + counter

    return f"the greater whole integer is: {counter}"
