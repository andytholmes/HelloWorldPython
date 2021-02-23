def list_less_than_10(num_array):
    ret_array = []
    for x in num_array:
        if x < 5:
            ret_array.append(x)
    return ret_array


def test_list_less_than_10():
    #Given
    input = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    #When
    actual = list_less_than_10(input)

    #Then
    assert actual == [1, 1, 2, 3]

