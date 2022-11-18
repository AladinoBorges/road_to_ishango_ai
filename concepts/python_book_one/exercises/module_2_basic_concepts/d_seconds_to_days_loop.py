from a_seconds_to_days import calculate_seconds_to_days


def get_seconds() -> int:
    seconds = eval(
        input(
            "please, insert the time in seconds (integer) that you want to calculate in days:\n-> "
        )
    )

    return seconds


def seconds_to_days_loop(stopValue: int = -1) -> str | ValueError:
    seconds = get_seconds()

    while seconds != stopValue:
        days = calculate_seconds_to_days(seconds)

        print(f"the number of corresponding days is: {days}.\n")

        seconds = get_seconds()
