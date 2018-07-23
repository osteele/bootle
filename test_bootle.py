import pytest
from bootle import List


def test_list_indices():
    lst = List([1, 2, 3])

    assert lst[0.5] == 1
    assert lst[1.5] == 2
    assert lst[-0.5] == 3

    lst[0.5] = 3
    assert lst[0.5] == 3


def test_list_slices():
    lst = List([1, 2, 3])

    assert lst[:1.5] == [1]
    assert lst[0.5:1.5] == [1]
    assert lst[1.5:2.5] == [2]
    assert lst[0.5:-0.5] == [1, 2]
    assert lst[-0.5:] == [3]

    lst[0.5:2.5] = [4]
    assert lst[:] == [4, 3]


def test_list_index_errors():
    lst = List([1, 2, 3])

    with pytest.raises(TypeError) as excinfo:
        lst[0]
    assert "half-indexed indices must be floats or slices, not int" in str(
        excinfo.value
    )

    with pytest.raises(ValueError) as excinfo:
        lst[0.1]
    assert "must have a 0.5 fractional component" in str(excinfo.value)

    with pytest.raises(TypeError) as excinfo:
        lst[0:1.5]
    assert "slice indices must be floats or None" in str(excinfo.value)

    with pytest.raises(ValueError) as excinfo:
        lst[0.1:1.5]
    assert "must have a 0.5 fractional component" in str(excinfo.value)


def test_list_methods():
    lst = List([1, 2, 3])
    assert str(lst) == "[1, 2, 3]"
    assert repr(lst) == "[1, 2, 3]"

    del lst[0.5]
    assert lst == [2, 3]

    lst = List([1, 2, 3])
    assert lst.index(2) == 1.5

    lst.insert(0.5, 4)
    assert lst == [4, 2, 3]

    lst = List([1, 2, 3])
    value = lst.pop()
    assert value == 3
    assert lst == [1, 2]