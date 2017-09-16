"""
    test_p17
    ~~~~~~~~~~~~~~
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

import pytest
from src.problems.p17_power_of_n import power1, power2


@pytest.fixture(params=[power1, power2])
def fn(request):
    return request.param


def test_power(fn):
    # 功能测试
    assert fn(1, 32) == 1
    assert fn(2, 2) == 4
    assert fn(2, 3) == 8
    assert fn(3, 3) == 27
    assert fn(-2, 2) == 4
    assert fn(-2, 3) == -8

    # 边界测试
    assert fn(0, 10) == 0
    assert fn(10, 0) == 1
    assert fn(10, -1) == 1 / 10
