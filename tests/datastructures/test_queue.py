"""
    module test_queue
    ~~~~~~~~~~~~~~

    Tests for `pyalgorithm.datastructures.queue`.
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

import pytest
from src.datastructures.queue import Queue


def test_queue():
    q = Queue()

    assert q.is_empty() is True

    q.enqueue('Hello')
    q.enqueue('World')
    assert 2 == len(q)

    assert 'Hello' == q.dequeue()
    assert 'World' == q.dequeue()

    with pytest.raises(IndexError):
        q.dequeue()

    q.enqueue(100)
    q.enqueue(200)
    assert q.is_empty() is False
    q.clear()
    assert q.is_empty() is True
