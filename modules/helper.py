def non_empty_string(s) -> str or None:
    """
    Used by reqparse module, to check weather the value is empty string or not
    :param s:
    :return: return string if not error
    """
    if not type(s) == str:
        raise ValueError("Must be string")
    if not s:
        raise ValueError("Must not be empty string")
    print('called!')
    return s


def extract_arguments(args: dict):
    """
    To extract arguments send from client
    :param args:
    :return:
    """
    return tuple([val for val in args.values()])
