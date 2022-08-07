# python
import nameof

def is_none(argument, argument_name):
    if argument is None:
        raise ValueError(f'\'{argument_name} was {nameof(None)}')