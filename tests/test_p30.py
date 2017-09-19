"""
    test_p30
    ~~~~~~~~~~~~~~
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

from src.problems.p30_middle_number_of_data_stream import get_medium


def test_get_medium():
    # 功能测试
    assert get_medium([1, 2, 3]) == 2
    assert get_medium([1, 2, 3, 4]) == 2.5
    assert get_medium(range(1, 10)) == 5

    # 特殊测试
    assert get_medium([]) is None
    assert get_medium([1]) == 1
    assert get_medium([1, 3]) == 2
    assert get_medium(None) is None

