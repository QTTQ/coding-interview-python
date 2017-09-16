"""
    test_p20
    ~~~~~~~~~~~~~~
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

from src.problems.p20_match_regex import match


def test_match():
    # 功能测试
    assert match('aaa', 'a.a') is True
    assert match('aaa', 'ab*ab*a') is True
    assert match('aaa', 'aa.a') is False
    assert match('aaa', 'ab*a') is False
    assert match('aaa', 'a.*a') is True

    # 特殊测试
    assert match('', '') is False
    assert match('', 'ab.c') is False
    assert match('aaa', '') is False
