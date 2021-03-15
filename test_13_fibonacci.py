import pytest


def get_fibonacci(sequence):
    if sequence == 1:
        return "1"

    if sequence == 2:
        return "1,1"

    fib_list = [1, 1]
    while sequence > 2:
        l = len(fib_list) - 1
        fib_list.append(fib_list[l] + fib_list[l - 1])
        sequence -= 1
    string_ints = [str(int) for int in fib_list]
    return ','.join(string_ints)



@pytest.mark.parametrize('seq_input, expected', [
    (1, "1"),
    (2, "1,1"),
    (3, "1,1,2"),
    (7, "1,1,2,3,5,8,13")])
def test_fibonacci(seq_input, expected):
    # Given

    # When
    actual = get_fibonacci(seq_input)

    # Then
    assert actual == expected

