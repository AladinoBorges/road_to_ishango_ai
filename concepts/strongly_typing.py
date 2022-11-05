def data_type_checker(data: any, target_type=str) -> dict[bool, str]:
    if type(data) != target_type:
        return {
            "status": False,
            "message": "invalid data. check your inputs and try again.",
        }

    return {"status": True, "message": "please, continue."}


def check_data_type(params_to_list: list) -> str | bool:
    for index, data in enumerate(params_to_list):
        print(index)
        if index == 0:
            is_valid_data = data_type_checker(data)

            if not is_valid_data["status"]:
                return is_valid_data["message"]
        else:
            is_valid_data = data_type_checker(data, int)

            if not is_valid_data["status"]:
                return is_valid_data["message"]
    return True


def my_name_is_and_age(name: str, birth_month: int, birth_year: int) -> str:
    params_to_list = [name, birth_month, birth_year]

    is_valid_data = check_data_type(params_to_list)

    if type(is_valid_data) != bool:
        return is_valid_data

    current_year_and_month: dict[str, int] = {"month": 11, "year": 2022}
    age: int = current_year_and_month["year"] - birth_year

    if birth_month > current_year_and_month["month"]:
        return f"hello {name}, you have {age - 1}"

    return f"hello {name}, you are {age} years old!"


print(my_name_is_and_age("Aladino", 7, 1991))
