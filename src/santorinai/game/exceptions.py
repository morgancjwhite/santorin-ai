class SantoriniGameException(Exception):
    """
    base exception for Santorini game module
    """


class InvalidGridReference(SantoriniGameException):
    """
    grid reference out of bounds (i.e. not in <A-e><1-5> format)
    """
    pass
