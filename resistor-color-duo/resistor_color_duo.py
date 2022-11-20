COLORS = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]


def color_code(color: str) -> int:
    """Return color code based on color name"""
    return COLORS.index(color.lower())


def value(colors: list[str]) -> int:
    """Return dual digits color code from a list of two names of colors"""
    first_color = color_code(colors[0])
    second_color = color_code(colors[1])

    return int(f"{first_color}{second_color}")
