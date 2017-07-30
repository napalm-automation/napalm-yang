from functools import wraps


def check_empty(default=''):
    """
    Decorator that checks if a value passed to a Jinja filter evaluates to false
    and returns an empty string. Otherwise calls the original Jinja filter.

    Example usage:
    @check_empty
    def my_jinja_filter(value, arg1):
    """
    def real_decorator(func):
        @wraps(func)
        def wrapper(value, *args, **kwargs):
            if not value:
                return default
            else:
                return func(value, *args, **kwargs)

        return wrapper
    return real_decorator
