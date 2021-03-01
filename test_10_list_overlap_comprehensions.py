import pytest

def get_list_intersect(list_one, list_two):
    return list(set([x for x in list_one if x in list_two]))

def test_get_list_intersect():
    #Given
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    expected = [1, 2, 3, 5, 8, 13]

    # When
    actual = get_list_intersect(a, b)

    # Then
    assert actual == expected
