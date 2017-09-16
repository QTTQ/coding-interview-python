"""
    test_p16
    ~~~~~~~~~~~~~~
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

import pytest
from src.problems.p16_number_of_one import number_of_one1, number_of_one2, number_of_one3


@pytest.fixture(params=[number_of_one1, number_of_one2, number_of_one3])
def fn(request):
    return request.param


def test_number_of_one(fn):
    assert fn(int('0', 2)) == 0
    assert fn(int('1', 2)) == 1
    assert fn(int('101010', 2)) == 3
    assert fn(int('1111', 2)) == 4
