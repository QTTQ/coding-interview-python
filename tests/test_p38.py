"""
    test_p38
    ~~~~~~~~~~~~~~
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

from src.problems.p38_find_missing_number import find_missing_number


def test_find_missing_number():
    assert find_missing_number([]) is None
    assert find_missing_number(None) is None
    assert find_missing_number([0, 1, 2]) == 3
    assert find_missing_number([1, 2, 3]) == 0
    assert find_missing_number([0, 2, 3]) == 1
    assert find_missing_number([0, 1, 3]) == 2
    assert find_missing_number([0]) == 1
