"""
    test_p34
    ~~~~~~~~~~~~~~
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

import pytest
from src.problems.p34_ugly_number import get_ugly_number_1, get_ugly_number_2


@pytest.fixture(params=[get_ugly_number_1, get_ugly_number_2])
def fn(request):
    return request.param


def test_get_ugly_number(fn):
    assert fn(0) is None
    assert fn(1) == 1
    assert fn(2) == 2
    assert fn(3) == 3
    assert fn(4) == 4
    assert fn(5) == 5
    assert fn(10) == 12
    assert fn(150) == 5832

    assert get_ugly_number_2(1500) == 859963392
