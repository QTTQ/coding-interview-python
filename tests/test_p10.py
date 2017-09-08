"""
    test_p10
    ~~~~~~~~~~~~~~

    Description of this module.
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

import pytest

from src.problems.p10_fibonacci import fibonacci1, fibonacci2, fibonacci3


@pytest.fixture(params=[fibonacci1, fibonacci2, fibonacci3])
def fib_func(request):
    return request.param


def test_fibonacci(fib_func):
    assert fib_func(0) == 0
    assert fib_func(1) == 1
    assert fib_func(2) == 1
    assert fib_func(3) == 2
    assert fib_func(10) == 55
    assert fib_func(20) == 6765
