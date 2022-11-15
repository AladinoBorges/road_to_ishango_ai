"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record: tuple[str, str]) -> str:
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """
    coordinate = record[1]

    return coordinate


def convert_coordinate(coordinate: str) -> tuple[str, str]:
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """
    result = tuple(coordinate)

    return result


def compare_records(
    azara_record: tuple[str, str], rui_record: tuple[str, tuple[str, str], str]
) -> bool:
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """
    azara_coordinate = convert_coordinate(get_coordinate(azara_record))
    rui_coordinate = get_coordinate(rui_record)

    return azara_coordinate == rui_coordinate


def create_record(
    azara_record: tuple[str, str], rui_record: tuple[str, tuple[str, str], str]
) -> tuple[str, str, str, tuple[str, str], str]:
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """
    if compare_records(azara_record, rui_record):
        return azara_record + rui_record

    return "not a match"


def serialize_record(record: tuple) -> tuple:
    result = tuple(value for index, value in enumerate(record) if index != 1)

    return result


def clean_up(combined_record_group: tuple) -> str:
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.

    The return statement should be a multi-lined string with items separated by newlines.

    (see HINTS.md for an example).
    """
    report = ""

    for record in combined_record_group:
        report += f"{serialize_record(record)}\n"

    return report
