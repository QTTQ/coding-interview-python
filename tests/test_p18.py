"""
    test_p18
    ~~~~~~~~~~~~~~
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

from src.problems.p18_delete_node_from_list import delete


def test_delete_node_from_list():
    # 功能测试
    assert delete([1, 2, 3, 4], 1) == [2, 3, 4]
    assert delete([1, 2, 3, 4], 2) == [1, 3, 4]
    assert delete([1, 2, 3, 4], 3) == [1, 2, 4]
    assert delete([1, 2, 3, 4], 4) == [1, 2, 3]

    # 特殊测试
    assert delete([], 1) == []
    assert delete(None, 1) is None
