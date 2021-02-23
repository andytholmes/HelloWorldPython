from io import StringIO

def odd_or_even():
    num = int(input("Enter Number:"))

    if (num % 2 == 0):
        return "Even"
    else:
        return "Odd"

def test_odd_or_even_odd(monkeypatch):
    #Given
    num= StringIO("7\n")
    monkeypatch.setattr('sys.stdin',num)

    #When
    actual = odd_or_even()

    #Then
    assert actual == "Odd"

def test_odd_or_even_even(monkeypatch):
    #Given
    num= StringIO("8\n")
    monkeypatch.setattr('sys.stdin',num)

    #When
    actual = odd_or_even()

    #Then
    assert actual == "Even"
