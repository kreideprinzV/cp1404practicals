"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from prac_06.car import Car

def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length

def run_tests():
    """Run the tests on the functions."""
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"

    test_car1 = Car()
    assert test_car1.fuel == 0, "Car does not set default fuel correctly"


    test_car2 = Car(fuel=10)
    assert test_car2.fuel == 10, "Car does not set custom fuel correctly"

def format_sentence(phrase):
    """
    Format the given phrase as a sentence.
    >>> format_sentence("hello")
    'Hello.'
    >>> format_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    >>> format_sentence("good morning")
    'Good morning.'
    """

    phrase = phrase[0].upper() + phrase[1:] if phrase else ""
    if not phrase.endswith('.'):
        phrase += '.'
    return phrase

if __name__ == "__main__":
    run_tests()
    doctest.testmod()
