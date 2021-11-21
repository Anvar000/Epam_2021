from unittest.mock import Mock, call

from homework3.task1 import cache


def test_smoke():
    """Testing usual behaviour"""

    @cache(times=2)
    def func(a, b, c=0, d=0):
        return (a ** b) ** 2 + c + d

    some = 10, 2

    assert 10005 == func(*some, c=2, d=3)
    assert 10009 == func(*some, c=4, d=5)
    assert 10009 == func(*some, c=4, d=5)
    assert 10009 == func(*some, c=4, d=5)


def test_cached():
    mock = Mock()
    cached_function = cache(times=2)(mock)
    cached_function(1, 3)
    cached_function(1, 3)
    cached_function(1, 3)
    cached_function(1, 3)
    assert mock.mock_calls == [call(1, 3), call(1, 3)]
