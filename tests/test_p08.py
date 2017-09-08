"""
    test_08
    ~~~~~~~~~~~~~~

    Description of this module.
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

import pytest
from src.problems.p08_impl_queue_with_two_stacks import Queue


def test_queue():
    q = Queue()
    q.append_tail(1)
    assert len(q) == 1
    assert 1 == q.pop_head()
    assert len(q) == 0

    q.append_tail(2)
    q.append_tail(3)
    q.append_tail(4)

    assert 2 == q.pop_head()
    assert 3 == q.pop_head()
    assert 4 == q.pop_head()

    with pytest.raises(RuntimeError):
        _ = q.pop_head()

    q.append_tail(10)
    q.append_tail(20)
    assert 10 == q.pop_head()
    q.append_tail(30)
    assert 20 == q.pop_head()
    assert 30 == q.pop_head()
