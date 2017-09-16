"""
    test_p15
    ~~~~~~~~~~~~~~
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

from src.problems.p15_cut_rope import max_product_after_cutting1, max_product_after_cutting2


def test_max_product_after_counting1():
    # 特殊测试
    assert max_product_after_cutting1(0) == 0
    assert max_product_after_cutting1(1) == 0
    assert max_product_after_cutting1(2) == 1
    assert max_product_after_cutting1(3) == 2

    # 功能测试
    assert max_product_after_cutting1(4) == 4
    assert max_product_after_cutting1(6) == 9
    assert max_product_after_cutting1(8) == 18


def test_max_product_after_cutting2():
    # 特殊测试
    assert max_product_after_cutting2(0) == 0
    assert max_product_after_cutting2(1) == 0
    assert max_product_after_cutting2(2) == 1
    assert max_product_after_cutting2(3) == 2

    # 功能测试
    assert max_product_after_cutting2(4) == 4
    assert max_product_after_cutting2(5) == 6
    assert max_product_after_cutting2(6) == 9
    assert max_product_after_cutting2(8) == 18
