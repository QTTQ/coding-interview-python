"""
    test_p24
    ~~~~~~~~~~~~~~
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

from src.problems.p24_merge_sorted_list import merge_two_sorted_list


def test_merge_two_sorted_list():
    # 功能测试
    assert merge_two_sorted_list([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_two_sorted_list([1, 5, 6], [2, 6]) == [1, 2, 5, 6, 6]
    assert merge_two_sorted_list([1, 2, 3], [0, 4]) == [0, 1, 2, 3, 4]
    assert merge_two_sorted_list([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]

    # 特殊测试
    assert merge_two_sorted_list([1, 2, 3], []) == [1, 2, 3]
    assert merge_two_sorted_list([1, 2, 3], None) == [1, 2, 3]
    assert merge_two_sorted_list(None, [1, 2, 3]) == [1, 2, 3]
    assert merge_two_sorted_list([], [1, 2, 3]) == [1, 2, 3]
    assert merge_two_sorted_list([], []) == []
    assert merge_two_sorted_list([1], [2]) == [1, 2]
