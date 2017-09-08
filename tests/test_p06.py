"""
    test_p06
    ~~~~~~~~~~~~~~

    Description of this module.
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

from src.problems.p06_merge_two_sorted_arrays import merge_two_sorted_arrays


def test_merge_two_sorted_arrays():
    # 临界条件
    assert merge_two_sorted_arrays(None, 0, None, 0) is None
    assert merge_two_sorted_arrays(None, 0, [], 0) is None
    assert merge_two_sorted_arrays([], 0, [], 0) is None
    assert merge_two_sorted_arrays([], 0, [], 0) is None
    assert merge_two_sorted_arrays([1, 2], 2, [], 0) == [1, 2]
    assert merge_two_sorted_arrays([], 0, [1, 2], 2) == [1, 2]

    # 构建测试数组
    assert merge_two_sorted_arrays([1, None], 1, [2], 1) == [1, 2]
    assert merge_two_sorted_arrays([2, None], 1, [1], 1) == [1, 2]
    assert merge_two_sorted_arrays([1, 2, None, None], 2, [3, 4], 2) == [1, 2, 3, 4]
    assert merge_two_sorted_arrays([3, 4, None, None], 2, [1, 2], 2) == [1, 2, 3, 4]
    assert merge_two_sorted_arrays([3, 4, 6, None, None], 3, [2, 5], 2) == [2, 3, 4, 5, 6]
    assert merge_two_sorted_arrays([1, 3, 5, None, None, None, None],
                                   3, [0, 2, 4, 6], 4) == [0, 1, 2, 3, 4, 5, 6]
