def get_all_prime_factors() -> str:
    number = eval(input("Escreva um inteiro positivo:\n-> "))
    divider = 2
    prime_factors: list = []

    while number != 1:
        if number % divider == 0:
            prime_factors.append(divider)

            number = number // divider

        else:
            divider = divider + 1

    print(f"Fatores primos:\n{prime_factors}")


get_all_prime_factors()
