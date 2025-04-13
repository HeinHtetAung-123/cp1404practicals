"""
CP1404/CP5632 Practical
Testing code using assert and doctest
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

    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"

    car = Car(fuel=10)
    assert car.fuel == 10,"Car should set fuel to the 10"
    car = Car()
    assert car.fuel == 0,"Car should set fuel to 0"

def format_a_sentence(phrase):
    # starting with a capital and ending with a single full stop.
    # Important: start with a function header and just use pass as the body
    # then add doctests for 3 tests:
    #   'hello' -> 'Hello.'
    #   'It is an ex parrot.' -> 'It is an ex parrot.'
    # and one more that you decide is a useful test.
    # Run your doctests and watch the tests fail.
    # Then write the body of the function so that the tests pass.
    """
        Format a phrase as a sentence, starting with a capital and ending with a single full stop.

        >>> format_a_sentence('hello')
        'Hello.'
        >>> format_a_sentence('It is an ex parrot.')
        'It is an ex parrot.'
        >>> format_a_sentence('this is fine')
        'This is fine.'
    """
    phrase  = phrase.strip()
    if not phrase.endswith('.'):
        phrase+='.'
    return phrase[0].upper() + phrase[1:]

run_tests()
doctest.testmod()