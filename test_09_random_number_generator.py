import random
from io import StringIO


def guess_number():
    random_number = random.randint(1, 9)
    i = 0
    while i != random_number:
        i = int(input('guess a number between 1 and 9'))
        if i == random_number:
            print('correct')
            return
        if i > random_number:
            print('too high')
        if i < random_number:
            print('too low')


def test_generate_random_correct(mocker, monkeypatch, capsys):
    #mocker
    #mocker in python can be used to inject behaviour directly into a function before it is called

    #monkeypatch
    #used to inject system behaviour. This could be user input (as in this case) or global system variuables, etc.

    #capsys
    #this allows us to capture system output


    #Given
    random_number = 5
    mocker.patch('random.randint', return_value=random_number)

    user_choice = StringIO("5\n")
    monkeypatch.setattr('sys.stdin', user_choice)

    # When
    guess_number()

    # Then
    captured = capsys.readouterr()
    assert captured.out == 'guess a number between 1 and 9correct\n'


def test_generate_random_too_high(mocker, monkeypatch, capsys):
    # mocker
    # mocker in python can be used to inject behaviour directly into a function before it is called

    # monkeypatch
    # used to inject system behaviour. This could be user input (as in this case) or global system variuables, etc.

    # capsys
    # this allows us to capture system output

    # Given
    random_number = 2
    mocker.patch('random.randint', return_value=random_number)

    user_choice = StringIO("5\n2\n")
    monkeypatch.setattr('sys.stdin', user_choice)

    # When
    guess_number()

    # Then
    captured = capsys.readouterr()
    assert captured.out == 'guess a number between 1 and 9too high\nguess a number between 1 and 9correct\n'

def test_generate_random_too_high(mocker, monkeypatch, capsys):
    # mocker
    # mocker in python can be used to inject behaviour directly into a function before it is called

    # monkeypatch
    # used to inject system behaviour. This could be user input (as in this case) or global system variuables, etc.

    # capsys
    # this allows us to capture system output

    # Given
    random_number = 2
    mocker.patch('random.randint', return_value=random_number)

    user_choice = StringIO("1\n2\n")
    monkeypatch.setattr('sys.stdin', user_choice)

    # When
    guess_number()

    # Then
    captured = capsys.readouterr()
    assert captured.out == 'guess a number between 1 and 9too low\nguess a number between 1 and 9correct\n'
