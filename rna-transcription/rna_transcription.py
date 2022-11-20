RNA_VALUES: list[dict] = [
    {"nucleotide": "g", "complement": "c"},
    {"nucleotide": "c", "complement": "g"},
    {"nucleotide": "t", "complement": "a"},
    {"nucleotide": "a", "complement": "u"},
]


def find_value(
    values: list[dict], target_value: str, target_key: str = "nucleotide"
) -> dict:
    """List method to find the first element that meets criteria and
    return that element or an empty string."""
    result = ""

    for value in values:
        if value[target_key] == target_value.lower():
            result = value["complement"].upper()
            break

    return result


def to_rna(dna_strand):
    """Transcribe DNA value(s) into RNA complement(s) and returns that transcription
    or an empty string."""
    result = ""

    if len(dna_strand) > 1:
        result = "".join(
            [find_value(RNA_VALUES, character) for character in dna_strand]
        )

    else:
        result = find_value(RNA_VALUES, dna_strand)

    return result
