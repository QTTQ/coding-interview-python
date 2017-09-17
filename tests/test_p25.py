"""
    test_p25
    ~~~~~~~~~~~~~~
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

from src.problems.p25_print_matrix_cw import visit_matrix_in_clockwise_order

func = visit_matrix_in_clockwise_order


def test_visit_matrix_clockwise_order():
    # 功能测试
    m1 = [
        [1, 2],
        [3, 4]
    ]
    assert list(func(m1, 2, 2)) == [1, 2, 4, 3]

    m2 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert list(func(m2, 3, 3)) == [1, 2, 3, 6, 9, 8, 7, 4, 5]

    m3 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    assert list(func(m3, 4, 4)) == [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]

    # 特殊测试
    assert list(func(None, 3, 4)) == []
    assert list(func([], 0, 0)) == []
    assert list(func([[1, 2, 3]], 0, 0)) == []
    assert list(func([[1, 2, 3]], 1, 3)) == [1, 2, 3]
    assert list(func([[1], [2], [3]], 3, 1)) == [1, 2, 3]
