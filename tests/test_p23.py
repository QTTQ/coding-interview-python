"""
    test_p23
    ~~~~~~~~~~~~~~
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

from src.problems.p23_reverse_list import reverse_list


def test_reverse_list():
    # 功能测试
    assert reverse_list([1, 3, 4]) == [4, 3, 1]
    assert reverse_list([1, 2]) == [2, 1]
    assert reverse_list([1]) == [1]
    assert reverse_list([2, 2, 2]) == [2, 2, 2]

    # 特殊测试
    assert reverse_list(None) is None
    assert reverse_list([]) is None
