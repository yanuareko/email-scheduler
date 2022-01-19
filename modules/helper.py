def non_empty_string(s):
    """Used by reqparse module, to check weather the value is empty string or not
    :param s: any
    :return: return the value without modification
    """
    if not type(s) == str:
        raise ValueError("Must be string")
    if not s:
        raise ValueError("Must not be empty string")
    return s


def extract_arguments(args: dict) -> tuple:
    """To extract arguments send from client
    :param args: result from parser.parse_args()
    :return: tuple of values from args
    """
    return tuple([val for val in args.values()])
