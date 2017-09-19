"""
    test_p31
    ~~~~~~~~~~~~~~
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

from src.problems.p31_max_sum_of_sub_seq import max_sum_of_sub_seq


def test_max_sum_of_sub_seq():
    # 功能测试
    assert max_sum_of_sub_seq([1, -2, 3, 10, -4, 7, 2, -5]) == 18
    assert max_sum_of_sub_seq([-1, -2, -3, -2]) == 0
    assert max_sum_of_sub_seq([1, 2, 3]) == 6

    # 特殊测试
    assert max_sum_of_sub_seq([]) is None
    assert max_sum_of_sub_seq(None) is None
