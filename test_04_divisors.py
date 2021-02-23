def get_divisors(number):
        num_array=[]
        i = number
        while i > 0:
            if number % i == 0:
                num_array.append(i)
            i -= 1
        return num_array

def test_get_divisors_1():
    #Given
    number = 1

    #When
    actual = get_divisors(number)

    #Then
    assert actual == [1]

def test_get_divisors_2():
    #Given
    number = 2

    #When
    actual = get_divisors(number)

    #Then
    assert actual == [2, 1]


def test_get_divisors_20():
    #Given
    number = 20

    #When
    actual = (get_divisors(number))

    #Then
    assert sorted(actual) == [1, 2, 4, 5, 10, 20]
