"""
    test_p14
    ~~~~~~~~~~~~~~
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

from src.problems.p14_robot_range_of_motion import moving_count


def test_moving_count():
    # 特殊条件测试
    assert moving_count(0, 10, 10) == 0
    assert moving_count(10, 0, 10) == 0
    assert moving_count(10, 10, -1) == 0

    # 边界条件测试
    assert moving_count(1, 10, 10) == 10
    assert moving_count(1, 10, 0) == 1
    assert moving_count(10, 1, 0) == 1

    # 基本功能测试
    assert moving_count(10, 10, 2) == 6
    assert moving_count(10, 10, 10) == 64

