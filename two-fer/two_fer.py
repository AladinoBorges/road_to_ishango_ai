def two_fer(name: str = "you") -> str:
    """If name, example: Alice, is passed:
    return message "One for Alice, one for me.";
    if not, return "One for you, one for me."
    """
    return f"One for {name}, one for me."
