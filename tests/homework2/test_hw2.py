from homework2.hw2 import major_and_minor_elem


def test_one_elem_list():
    assert 13, 13 == major_and_minor_elem([13])


def test_several_elem__list():
    assert 2, 1 == major_and_minor_elem([2, 2, 1, 1, 1, 2, 2])
