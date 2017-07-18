def check_empty(filter_function):
    """
    Decorator that checks if a value passed to a Jinja filter evaluates to false
    and returns an empty string. Otherwise calls the original Jinja filter.

    Example usage:
    @check_empty
    def my_jinja_filter(value, arg1):
    """
    def wrapper(value, *args, **kwargs):
        if not value:
            return ''
        else:
            return filter_function(value, *args, **kwargs)

    return wrapper
