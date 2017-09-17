"""
    test_p26
    ~~~~~~~~~~~~~~
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

from src.problems.p26_min_stack import Stack


def test_min_stack():
    s = Stack()
    s.push(10)
    assert s.min() == 10
    s.push(20)
    assert s.min() == 10
    s.push(5)
    assert s.min() == 5

    assert s.pop() == 5
    assert s.min() == 10

    s.push(-10)
    assert s.min() == -10
    s.push(-20)
    assert s.min() == -20

    assert s.pop() == -20
    assert s.min() == -10
    assert s.pop() == -10
    assert s.min() == 10
