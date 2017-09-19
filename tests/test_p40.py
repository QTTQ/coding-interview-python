"""
    test_p40
    ~~~~~~~~~~~~~~
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

import pytest
from src.problems.p40_two_sum import two_simple_stupid_way


@pytest.fixture(params=[two_simple_stupid_way])
def fn(request):
    return request.param


def test_two_sum(fn):
    assert fn(10, None) is None
    assert fn(1, []) is None
    assert tuple(fn(7, [1, 2, 3, 4, 5])) in [(3, 4), (2, 5)]
    assert fn(8, [1, 2, 3]) is None
