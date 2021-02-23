def is_palindrome(pal_string):

    #if ''.join(reversed(list(pal_string))) == pal_string:
    if pal_string[::-1] == pal_string:
        return True
    else:
        return False


def test_is_palindrome_True():
    # Given
    test_string = 'MUM'

    # When
    result = is_palindrome(test_string)

    # Then
    assert result

def test_is_palindrome_False():
    # Given
    test_string = 'MUD'

    # When
    result = is_palindrome(test_string)

    # Then
    assert not result

