def get_integer() -> int | str | bool:
    user_input = eval(
        input("please, insert an integer or '-1' to close the program:\n-> ")
    )

    if not isinstance(user_input, int):
        print("please, inserto only integers equal or greater than 0.")
        get_integer()

    return user_input


def calculate_whole_integer() -> int | str | bool:
    numbers = ""
    user_input = get_integer()

    while user_input != -1:
        numbers += str(user_input)

        user_input = get_integer()

    if len(numbers) > 0:
        return f"inserted number: {int(numbers)}"

    return "no valid integers inserted."
