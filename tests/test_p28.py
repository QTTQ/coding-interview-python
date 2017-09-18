"""
    test_p28
    ~~~~~~~~~~~~~~
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

import pytest
from src.problems.p28_num_occurs_more_than_others import find_number_stupid_way, \
    find_number_smart_way


@pytest.fixture(params=[find_number_smart_way, find_number_stupid_way])
def fn(request):
    return request.param


def test_find_number(fn):
    # 功能测试
    assert fn([1]) == 1
    assert fn([2, 2, 2]) == 2
    assert fn([1, 2, 3, 2, 2, 2]) == 2
    assert fn([1, 2, 3, 2, 2]) == 2
    assert fn([1, 2, 3, 2, 2, 2, 5, 4, 2]) == 2

    # 特殊测试
    assert fn(None) is None
    assert fn([]) is None
    assert fn([1, 2, 3]) is None
