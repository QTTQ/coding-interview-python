"""
    test_p42
    ~~~~~~~~~~~~~~
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

import pytest
from src.problems.p42_max_queue import QueueWithMax


def test_queue_with_max():
    queue = QueueWithMax()
    assert queue.empty() is True
    assert len(queue) == 0

    queue.put(10)
    queue.put(20)
    assert queue.maxvalue == 20
    assert queue.get() == 10
    assert len(queue) == 1
    assert queue.get() == 20

    with pytest.raises(IndexError):
        _ = queue.get()
        _ = queue.maxvalue

    queue.put(12)
    queue.put(9)
    queue.put(4)
    queue.put(8)

    assert queue.maxvalue == 12
    assert queue.get() == 12
    assert queue.maxvalue == 9
    assert queue.get() == 9
    assert queue.maxvalue == 8
    assert queue.get() == 4
    assert queue.get() == 8
    assert queue.empty() is True
