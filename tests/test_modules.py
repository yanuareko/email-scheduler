from modules.helper import non_empty_string, extract_arguments, wanted_time_format


def test_non_empty():
    assert non_empty_string('any_string') == 'any_string'


def test_extract_argument():
    assert extract_arguments({'one': 1, 'two': 2}) == (1, 2)


def test_wanted_time_format():
    assert wanted_time_format("2022-01-20T18:17")
