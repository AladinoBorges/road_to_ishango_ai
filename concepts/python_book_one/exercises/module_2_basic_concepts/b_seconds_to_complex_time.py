HOUR_IN_SECONDS = 60 * 60
DAY_IN_SECONDS = HOUR_IN_SECONDS * 24


def calculate_days(seconds: int) -> dict[str, int]:
    days = seconds // DAY_IN_SECONDS
    remainder = seconds % DAY_IN_SECONDS

    return {"days": days, "remainder": remainder}


def calculate_hours(seconds: int) -> dict[str, int]:
    hours = seconds // HOUR_IN_SECONDS
    remainder = seconds % HOUR_IN_SECONDS

    return {"hours": hours, "remainder": remainder}


def calculate_minutes_and_seconds(seconds: int) -> list[int]:
    minutes = seconds // 60
    seconds = seconds % 60

    return [minutes, seconds]


def calculate_time(seconds: int) -> list[int]:
    days_and_remainder = calculate_days(seconds)
    hours_and_remainder = calculate_hours(days_and_remainder["remainder"])
    minutes_and_seconds = calculate_minutes_and_seconds(days_and_remainder["remainder"])

    days = days_and_remainder["days"]
    hours = hours_and_remainder["hours"]

    return [days, hours, *minutes_and_seconds]


def serialize_time_data(values: list[int]) -> str:
    [days, hours, minutes, seconds] = values

    return f"dias: {days} horas: {hours} mins: {minutes} segs: {seconds}"


def seconds_to_complex_time() -> float | ValueError:
    try:
        seconds: int = int(
            input("insert the number of seconds that you want to calculate:\n-> ")
        )

        if seconds <= 0:
            raise ValueError("Error:\n")

        else:
            time = calculate_time(seconds)

            return serialize_time_data(time)
    except ValueError:
        return "number needs to be an integer and greater than zero."
