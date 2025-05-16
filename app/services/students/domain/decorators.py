import re
from app.proj_utils.app_logger import error, info, debug

def length(min_length:int, max_length:int):
    """
    Decorator to validate the length of a string attribute.
    
    :param min_length: Minimum length of the string.
    :param max_length: Maxinum length of the string.
    :return: Decorated function.
    :raises ValueError: If the value does not meet the length requirements.
    """
    def decorator(func):
        def wrapper(self, value):
            if not (min_length <= len(value) <= max_length):
                error(f"Value must be between {min_length} and {max_length} characters.")
                raise ValueError(f"Value must be between {min_length} and {max_length} characters.")
            return func(self, value)
        return wrapper
    return decorator

def not_none():
    """
    Decorator to validate a property is not None.
    
    :return: Decorated function.
    :raises ValueError: If the value is of the None type.
    """
    def decorator(func):
        def wrapper(self, value):
            if value is None:
                error("Value must not be None type")
                raise ValueError("Value must not be None type")
        return wrapper
    return decorator

def not_blank():
    """
    Decorator to validate a property is not blank. This function checks for 'None', the empty str '', and the None type.
    
    :return: Decorated function.
    :raises ValueError: If the value is of the type.
    """
    def decorator(func):
        def wrapper(self, value):
            if value is None:
                error("Value must not be None type")
                raise ValueError("Value must not be None type")
            if value == 'None':
                error("Value must not be 'None' str")
                raise ValueError("Value must not be 'None' str")
            if value == '':
                error("Value must not be '' str")
                raise ValueError("Value must not be '' str")
            return func(self, value)
        return wrapper
    return decorator

def is_numeric():
    """
    Decorator to validate that a str property is numeric (0-9).
    
    :return: Decorated function.
    :raises: ValueError: If the value is not numeric.
    """
    def decorator(func):
        def wrapper(self, value):
            numeric = re.match('^[0-9]+$',value)
            if not numeric:
                error("only numeric (0-9) values may be used")
                raise ValueError("only numeric (0-9) values may be used")
            return func(self, value)
        return wrapper
    return decorator

def email():
    """
    Decorator to validate that a str exists is in email format.
    
    :return: Decorated function.
    :raises ValueError: If the value is not in email format.
    """
    def decorator(func):
        def wrapper(self, value):
            email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            email_formatted = re.match(email_pattern, value)
            if not email_formatted:
                error(f"The email address: '{value}' is not email formatted.")
                raise ValueError(f"The email address: '{value}' is not email formatted.")
            return func(self, value)
        return wrapper
    return decorator