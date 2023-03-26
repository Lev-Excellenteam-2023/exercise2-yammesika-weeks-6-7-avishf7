from functools import wraps


class InvalidType(Exception):
    """
    Custom exception class for indicating that an argument is of an invalid type.
    """


def type_check(correct_type):
    """
    A decorator that checks if the argument passed to a function is of the correct type.

    :param correct_type: The correct type that the argument should be of.
    :return: A decorator function that checks if the argument is of the correct type.
    :raises InvalidType: If the argument is not of the correct type.
    """
    def decorator(func):
        @wraps(func)
        def check_wrapper(arg):
            if type(arg) is correct_type:
                return func(arg)
            else:
                raise InvalidType(f"expected {correct_type}, but given {type(arg)}")
        return check_wrapper
    return decorator
