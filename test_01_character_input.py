from io import StringIO

def character_input():
    name = input("Please enter your name:")
    age = input("Please enter your age:")
    return 'Your name is ' + name + ". You are " + age + " years old."

def test_character_input(monkeypatch):
    # Given
    input = StringIO("Andrew\n40\n")

    # When
    monkeypatch.setattr('sys.stdin', input)

    # Then
    i = character_input()
    assert i == "Your name is Andrew. You are 40 years old."


