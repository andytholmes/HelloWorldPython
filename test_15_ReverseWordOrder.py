import pytest

def reverse_word_order(words):

    return ' '.join(words.split()[::-1])

def test_reverse_word_order_hello():
    # Given
    expected = 'hello'

    # When
    actual = reverse_word_order('hello')

    # Then
    assert expected == actual

def test_reverse_word_order_hello_world():
    # Given
    expected = 'world hello'

    # When
    actual = reverse_word_order('hello world')

    # Then
    assert expected == actual

def test_reverse_word_order_this_is_a_complicated_sentence():
    # Given
    expected = 'sentence complicated a is this'

    # When
    actual = reverse_word_order('this is a complicated sentence')

    # Then
    assert expected == actual
