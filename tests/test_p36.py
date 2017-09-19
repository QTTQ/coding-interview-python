"""
    test_p36
    ~~~~~~~~~~~~~~
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

import pytest
from src.problems.p36_find_first_common_node import (find_first_common_node_1,
                                                     find_first_common_node_2,
                                                     build_two_list_with_common_nodes)


@pytest.fixture(params=[find_first_common_node_1,
                        find_first_common_node_2])
def fn(request):
    return request.param


def test_find_first_common_node(fn):
    h1, h2 = build_two_list_with_common_nodes([1, 2, 3], [4, 5, 6], [10, 11])
    assert fn(h1, h2) == 10

    h1, h2 = build_two_list_with_common_nodes([1, 2], [4, 5, 6], [10, 11])
    assert fn(h1, h2) == 10
    assert fn(h2, h1) == 10

    h1, h2 = build_two_list_with_common_nodes([1], [4], [10])
    assert fn(h1, h2) == 10

    h1, h2 = build_two_list_with_common_nodes([1, 2, 3], [4, 5])
    assert fn(h1, h2) is None

    assert fn(h1, None) is None
    assert fn(None, None) is None
