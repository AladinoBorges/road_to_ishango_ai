def seconds_to_days() -> float:
    seconds: int = eval(
        input("Insert the number of seconds that you want to calculate:\n-> ")
    )

    base_seconds = 60
    base_minutes = 1 * base_seconds
    base_hour = base_minutes * base_seconds
    base_day = 24 * base_hour

    total_days = seconds / base_day

    return total_days
