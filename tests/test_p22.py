"""
    test_p22
    ~~~~~~~~~~~~~~
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

from src.problems.p22_find_entry_of_partial_circular_list import \
    find_entry_in_partial_circle_list


def test_find_entry():
    # 功能测试
    # 1. 不存在环的情况
    assert find_entry_in_partial_circle_list([1, 2, 3, 4], None) is None
    # 2. 环入口在开头
    assert find_entry_in_partial_circle_list([1, 2, 3, 4], 1) == 1
    # 3. 环入口在中间
    assert find_entry_in_partial_circle_list([1, 2, 3, 4, 5], 3) == 3
    # 4. 环入口在尾部
    assert find_entry_in_partial_circle_list([1, 2, 3, 4, 5], 5) == 5

    # 特殊测试
    assert find_entry_in_partial_circle_list([], None) is None
    assert find_entry_in_partial_circle_list(None, None) is None
    assert find_entry_in_partial_circle_list([1], None) is None
    assert find_entry_in_partial_circle_list([1], 1) == 1
    assert find_entry_in_partial_circle_list([1, 2], 2) == 2
    assert find_entry_in_partial_circle_list([1, 2, 3], 2) == 2


if __name__ == '__main__':
    test_find_entry()
