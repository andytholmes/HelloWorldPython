def get_list_ends(list_of_numbers):
    return [list_of_numbers[0],list_of_numbers[len(list_of_numbers)-1]]

def test_get_list_ends():
    # Given
    list_of_numbers = [5, 10, 15, 20, 25, 30]
    expected = [5, 30]

    # When
    actual = get_list_ends(list_of_numbers)

    # Then
    assert actual == expected