"""
    test_p41
    ~~~~~~~~~~~~~~
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

import pytest
from src.problems.p41_find_max_in_sliding_window import (MaxStack, MaxQueue,
                                                         max_values_of_sliding_window_1,
                                                         max_values_of_sliding_window_2)


def test_max_stack():
    stack = MaxStack()
    assert len(stack) == 0
    assert stack.maxvalue() is None
    stack.push(10)
    assert stack.maxvalue() == 10
    stack.push(11)
    assert stack.maxvalue() == 11

    stack.push(18)
    assert stack.maxvalue() == 18

    assert 18 == stack.pop()
    assert stack.maxvalue() == 11

    assert 11 == stack.pop()
    assert stack.maxvalue() == 10
    assert len(stack) == 1


def test_max_queue():
    queue = MaxQueue(2)
    assert len(queue) == 0
    assert queue.full() is False

    queue.put(10)
    queue.put(20)
    assert queue.full() is True
    # [10, 20]
    assert queue.maxvalue() == 20

    queue.put(8)
    # [20, 8]
    assert queue.maxvalue() == 20

    queue.put(4)
    # [8, 4]
    assert queue.maxvalue() == 8

    queue.put(10)
    # [4, 10]
    assert queue.maxvalue() == 10


@pytest.fixture(params=[max_values_of_sliding_window_1,
                        max_values_of_sliding_window_2])
def fn(request):
    return request.param


def test_max_values_of_sliding_window(fn):
    assert fn(0, [1, 2, 3]) is None
    assert fn(2, None) is None
    assert fn(2, [1]) is None

    # 功能测试
    assert fn(1, [1, 6, 2, 8, 10]) == [1, 6, 2, 8, 10]
    assert fn(2, [1, 6, 2, 8, 10]) == [6, 6, 8, 10]
    assert fn(3, [1, 6, 2, 8, 10]) == [6, 8, 10]
    assert fn(4, [1, 6, 2, 8, 10]) == [8, 10]
    assert fn(5, [1, 6, 2, 8, 10]) == [10]
    assert fn(3, [2, 3, 4, 2, 6, 2, 5, 1]) == [4, 4, 6, 6, 6, 5]
