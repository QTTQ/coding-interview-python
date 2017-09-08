"""
    test_p11
    ~~~~~~~~~~~~~~
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

import pytest
from src.problems.p11_sort_ages import sort_ages


def test_sort_ages():
    assert sort_ages(None) is None
    assert sort_ages([20]) == [20]
    assert sort_ages([20, 30, 19]) == [19, 20, 30]
    assert sort_ages([20, 30, 19, 20]) == [19, 20, 20, 30]
    assert sort_ages([30, 40, 20, 30, 50, 60, 20]) == [20, 20, 30, 30, 40, 50, 60]

    with pytest.raises(ValueError):
        sort_ages([10])
