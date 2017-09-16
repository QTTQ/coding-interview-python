"""
    module test_deque
    ~~~~~~~~~~~~~~

    Tests for `pyalgorithm.datastructures.deque`.
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

import pytest
from src.datastructures.deque import Deque


def test_deque():
    q = Deque()
    assert q.is_empty() is True

    q.append_front('Hello')
    q.append_front('World')
    assert len(q) == 2

    q.append_rear('Happy')
    q.append_rear('Coding')
    assert len(q) == 4

    # World, Hello, Happy, Coding
    assert 'World' == q.pop_front()
    assert 'Coding' == q.pop_rear()
    assert 'Happy' == q.pop_rear()
    assert 'Hello' == q.pop_rear()

    with pytest.raises(IndexError):
        q.pop_rear()

    with pytest.raises(IndexError):
        q.pop_front()

    q.append_rear('Hello')
    assert q.is_empty() is False

    q.clear()
    assert q.is_empty() is True
