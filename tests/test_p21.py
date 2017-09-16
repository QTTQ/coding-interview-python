"""
    test_p21
    ~~~~~~~~~~~~~~
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

from src.problems.p21_adjust_odd_even_nums_in_array import (adjust_odd_even_nums_order,
                                                            adjust_odd_even_nums_order1,
                                                            reorder, is_even)


def test_adjust_odd_even_nums_order():
    # 功能测试
    assert adjust_odd_even_nums_order([2, 1]) == [1, 2]
    assert adjust_odd_even_nums_order([1, 2, 3]) == [1, 3, 2]
    assert adjust_odd_even_nums_order([1, 2, 3, 4]) == [1, 3, 2, 4]
    assert adjust_odd_even_nums_order([2, 1, 9, 8, 10]) == [9, 1, 2, 8, 10]

    # 特殊测试
    assert adjust_odd_even_nums_order([]) == []
    assert adjust_odd_even_nums_order(None) is None
    assert adjust_odd_even_nums_order([1, 3, 5]) == [1, 3, 5]
    assert adjust_odd_even_nums_order([2, 4, 6]) == [2, 4, 6]
    assert adjust_odd_even_nums_order([1, 3, 5, 2, 4, 6]) == [1, 3, 5, 2, 4, 6]


def test_adjust_odd_even_nums_order1():
    # 功能测试
    assert adjust_odd_even_nums_order1([2, 1]) == [1, 2]
    assert adjust_odd_even_nums_order1([1, 2, 3]) == [1, 3, 2]
    assert adjust_odd_even_nums_order1([1, 2, 3, 4]) == [1, 3, 2, 4]
    assert adjust_odd_even_nums_order1([2, 1, 9, 8, 10]) == [9, 1, 2, 8, 10]

    # 特殊测试
    assert adjust_odd_even_nums_order1([]) == []
    assert adjust_odd_even_nums_order1(None) is None
    assert adjust_odd_even_nums_order1([1, 3, 5]) == [1, 3, 5]
    assert adjust_odd_even_nums_order1([2, 4, 6]) == [2, 4, 6]
    assert adjust_odd_even_nums_order1([1, 3, 5, 2, 4, 6]) == [1, 3, 5, 2, 4, 6]


def test_reorder():
    from functools import partial
    partial_reorder = partial(reorder, func=is_even)

    # 功能测试
    assert partial_reorder([2, 1]) == [1, 2]
    assert partial_reorder([1, 2, 3]) == [1, 3, 2]
    assert partial_reorder([1, 2, 3, 4]) == [1, 3, 2, 4]
    assert partial_reorder([2, 1, 9, 8, 10]) == [9, 1, 2, 8, 10]

    # 特殊测试
    assert partial_reorder([]) == []
    assert partial_reorder(None) is None
    assert partial_reorder([1, 3, 5]) == [1, 3, 5]
    assert partial_reorder([2, 4, 6]) == [2, 4, 6]
    assert partial_reorder([1, 3, 5, 2, 4, 6]) == [1, 3, 5, 2, 4, 6]