import pytest

def is_prime(number):
    i = number-1
    while (i > 1):
        if number%i == 0:
            return False
        i -= 1
    return True


@pytest.mark.parametrize('number, expected_prime', [
    (13, True),
    (7, True),
    (8, False)
])
def test_is_prime(number, expected_prime):
    # Given

    # When
    actual = is_prime(number)

    # Then
    assert actual is expected_prime
