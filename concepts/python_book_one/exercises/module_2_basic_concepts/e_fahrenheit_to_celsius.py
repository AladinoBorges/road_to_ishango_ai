def fahrenheit_to_celsius_converter(temperature: int) -> float:
    return round((5 / 9) * (temperature - 32), 2)


def print_formatted_data(data: list) -> str:
    print("{: <8} {: <16} {: <16}".format(*data))


def print_temperature_table_from_range(start: int = 40, end: int = 120) -> str:
    headers = ["index", "fahrenheit", "celsius"]

    print_formatted_data(headers)

    for index, temperature in enumerate(range(start, end + 1)):
        rows = [
            index + 1,
            f"{temperature}°",
            f"{fahrenheit_to_celsius_converter(temperature)}°",
        ]

        print_formatted_data(rows)
