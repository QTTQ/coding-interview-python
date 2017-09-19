"""
    test_p35
    ~~~~~~~~~~~~~~
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

from src.problems.p35_first_not_repeating_char import first_not_repeating_char_in_string


def test_first_not_repeating_char_in_string():
    assert first_not_repeating_char_in_string('abcabeff') == 'c'
    assert first_not_repeating_char_in_string('abccabeff') == 'e'
    assert first_not_repeating_char_in_string('abcd') == 'a'
    assert first_not_repeating_char_in_string('aabbccddd') is None
    assert first_not_repeating_char_in_string(None) is None
    assert first_not_repeating_char_in_string('') is None


