"""
    test_p33
    ~~~~~~~~~~~~~~
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

from src.problems.p33_longest_non_repeat_seq import longest_unique_substr


def test_longest_unique_substr():
    assert longest_unique_substr('a') == 1
    assert longest_unique_substr('aaaa') == 1
    assert longest_unique_substr('arabcacfr') == 4
    assert longest_unique_substr('pwwkew') == 3
    assert longest_unique_substr('abcabcbb') == 3

    assert longest_unique_substr('') == 0
    assert longest_unique_substr(None) == 0
