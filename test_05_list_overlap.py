def find_list_overlap(a, b):
    return list(set(a) & set(b))

def test_find_list_overlap_1():
    #Given
    a= [1]
    b = [1]

    # When
    result = find_list_overlap(a, b)

    # Then
    assert result == [1]

def test_find_list_overlap_duplicates():
    #Given
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    # When
    result = find_list_overlap(a, b)

    # Then
    assert result == [1, 2, 3, 5, 8, 13]
