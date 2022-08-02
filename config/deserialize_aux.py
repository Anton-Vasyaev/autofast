def is_generic(t):
    return hasattr(t, '__origin__')


def is_list_alias(t):
    return t.__origin__ == list if is_generic(t) else False


def is_tuple_alias(t):
    return t.__origin__ == tuple if is_generic(t) else False


def get_list_alias_arg(t):
    return t.__args__[0]


def get_tuple_alias_args(t):
    return t.__args__