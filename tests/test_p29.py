"""
    test_p29
    ~~~~~~~~~~~~~~
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

import pytest
from src.problems.p29_n_smallest_numbers import (n_smallest_numbers,
                                                 n_smallest_numbers1)


@pytest.fixture(params=[n_smallest_numbers1, n_smallest_numbers])
def n_smallest(request):
    return request.param


def test_n_smallest_numbers(n_smallest):
    # 功能测试
    assert set(n_smallest(2, [1, 2, 3, 4, 5])) == {1, 2}
    assert set(n_smallest(5, list(range(1000)))) == {0, 1, 2, 3, 4}

    # 特殊测试
    assert set(n_smallest(1, [1])) == {1}
    assert n_smallest(2, [1]) is None
    assert n_smallest(1, None) is None
