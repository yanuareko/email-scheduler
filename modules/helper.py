import re


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


def wanted_time_format(text: any) -> any:
    result = re.findall(r"(\d{4}-\d{2}-\d{2}T\d{2}:\d{2})", str(text))
    if not result:
        raise ValueError("Format not match, example: 2006-01-02T15:04")
    return text
