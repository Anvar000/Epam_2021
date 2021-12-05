import pytest

from homework5.save_original_info import custom_sum


def test_doc_printing():
    actual_doc = "This function can sum any objects which have __add___"
    assert custom_sum.__doc__ == actual_doc


def test_name_printing():
    assert custom_sum.__name__ == "custom_sum"


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ((1, 2, 3, 4), 10),
        (([1, 2, 3], [4, 5]), [1, 2, 3, 4, 5]),
        (("a", "bc"), "abc")
        ]
)
def test_result_printing(value, expected_result):
    assert custom_sum(*value) == expected_result
