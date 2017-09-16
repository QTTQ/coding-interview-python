"""
    test_p19
    ~~~~~~~~~~~~~~
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

from src.problems.p19_remove_duplicate_nodes_from_list import remove_duplicates


def test_remove_duplicates():
    # 功能测试
    assert remove_duplicates([1, 1, 2]) == [1, 2]
    assert remove_duplicates([1, 1, 2, 3, 3]) == [1, 2, 3]
    assert remove_duplicates([1, 1, 1]) == [1]
    assert remove_duplicates([1, 2, 3]) == [1, 2, 3]
    assert remove_duplicates([1, 1, 2, 3, 4, 4]) == [1, 2, 3, 4]

    # 特殊测试
    assert remove_duplicates([]) == []
    assert remove_duplicates(None) is None
    assert remove_duplicates([1]) == [1]
