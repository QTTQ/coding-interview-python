"""
    test_p27
    ~~~~~~~~~~~~~~
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

from src.problems.p27_push_pop_sequence_in_stack import is_possible_out_sequence


def test_is_possible_out_sequence():
    # 功能测试
    assert is_possible_out_sequence([1], [1]) is True
    assert is_possible_out_sequence([1, 2, 3, 4], [4, 3, 2, 1]) is True
    assert is_possible_out_sequence([1, 2, 3, 4], [2, 1, 4, 3]) is True
    assert is_possible_out_sequence([1, 2, 3, 4], [2, 1, 4, 3]) is True
    assert is_possible_out_sequence([1, 2, 3, 4, 5], [4, 3, 5, 2, 1]) is True
    assert is_possible_out_sequence([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]) is False

    # 特殊测试
    assert is_possible_out_sequence([], [2]) is False
    assert is_possible_out_sequence([], []) is False
    assert is_possible_out_sequence([1, 2], []) is False
    assert is_possible_out_sequence(None, None) is False
