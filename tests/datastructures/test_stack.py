"""
    module test_stack
    ~~~~~~~~~~~~~~

    Tests for the stack data structure.
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

import pytest

from src.datastructures.stack import DequeStack, ListStack


@pytest.fixture(params=[DequeStack, ListStack])
def stack(request):
    return request.param()


def test_stack(stack):
    stack.push(10)
    stack.push(11)
    stack.push(12)
    assert 12 == stack.peek()
    assert 3 == len(stack)
    assert stack.is_empty() is False

    assert 12 == stack.pop()
    assert 11 == stack.pop()
    assert 10 == stack.pop()
    assert stack.is_empty() is True

    import pytest
    with pytest.raises(IndexError):
        stack.pop()

    stack.push(0)
    stack.push(1)
    assert stack.is_empty() is False
    stack.clear()
    assert stack.is_empty() is True

if __name__ == '__main__':
    test_stack(DequeStack())
    test_stack(ListStack())
