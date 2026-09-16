def search4letters(phrase, letters="aeiou"):
    """return the set of the letter found in te phrase."""
    return set(letters).intersection(set(phrase))
