def search4letters(phrase: str, letters="aeiou"):
    """return the set of the letter found in te phrase."""
    return set(letters).intersection(set(phrase))
