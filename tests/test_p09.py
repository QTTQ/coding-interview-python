"""
    test_p09
    ~~~~~~~~~~~~~~

    Description of this module.
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

import pytest

from src.problems.p09_impl_stack_with_two_queues import Stack


def test_stack():
    s = Stack()
    assert 0 == len(s)

    # 入栈 3->2->1
    s.push(1)
    s.push(2)
    s.push(3)

    assert len(s) == 3

    # 出栈
    assert 3 == s.pop()
    assert 2 == s.pop()

    # 5 入栈：5->1
    s.push(5)
    assert 5 == s.pop()
    assert 1 == s.pop()

    assert 0 == len(s)

    with pytest.raises(RuntimeError):
        _ = s.pop()
