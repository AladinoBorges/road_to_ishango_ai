def whole_integer_digits_sum() -> str:
    counter = 0

    number = eval(input("Escreva um inteiro positivo:\n-> "))

    while number > 0:
        digit = number % 10  # gets the unitary algarisme
        number = number // 10  # removes the algarisme from all unities

        counter = counter + digit

    print("Soma dos dígitos:", counter)
