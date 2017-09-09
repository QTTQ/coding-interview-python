"""
    test_p12
    ~~~~~~~~~~~~~~
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

import pytest
from src.problems.p12_find_smallest_in_rotated_array import find_smallest_number1


@pytest.fixture(params=[find_smallest_number1])
def func(request):
    return request.param


def test_find_smallest_number(func):
    assert func(None) is None
    assert func([]) is None
    assert func([1]) == 1
    assert func([1, 2, 3]) == 1
    assert func([1, 0, 1, 1, 1]) == 0
    assert func([1, 1, 1, 0, 1]) == 0
    assert func([3, 4, 5, 1, 2]) == 1
    assert func([3, 4, 5, 1, 1]) == 1
