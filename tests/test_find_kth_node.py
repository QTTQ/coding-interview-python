"""
    test_find_kth_node
    ~~~~~~~~~~~~~~
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

import pytest
from src.datastructures.linkedlist.single import List
from src.problems.p01_find_kth_node import find_kth_node


@pytest.mark.parametrize('seq, k, expected',
                         [
                             (None, 1, None),
                             ([], 1, None),
                             ([1], 1, 1),
                             ([1, 2, 3], 0, None),
                             ([1, 2, 3], 1, 3),
                             ([1, 2, 3], 2, 2),
                             ([1, 2, 3], 3, 1),
                             ([1, 2, 3], 4, None),
                         ])
def test_find_kth_node(seq, k, expected):
    head = List.fromvalues(seq).head if seq else None
    if expected is None:
        assert find_kth_node(head, k) is None
    else:
        assert find_kth_node(head, k).val == expected
