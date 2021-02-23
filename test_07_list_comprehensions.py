def get_even_in_array(num_array):
    return [x for x in num_array if x % 2 == 0]

def test_get_even_in_array():
    # Given
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    # When
    actual = get_even_in_array(a)

    # Then
    assert actual == [4, 16, 36, 64, 100]



