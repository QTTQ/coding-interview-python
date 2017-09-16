"""
    module test_linked_list
    ~~~~~~~~~~~~~~

    Tests for `pyalgorithm.datastructures.linklist`
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

import pytest
from src.datastructures.linkedlist.single import List as LinkedList


def test_create_linked_list_from_values():
    values = [1, 2, 3, 4]
    l = LinkedList.fromvalues(values)
    assert list(l) == values
    assert len(l) == len(values)


def test_list_contains_x():
    values = [1, 2, 3, 4]
    l = LinkedList.fromvalues(values)
    assert 1 in l
    assert 3 in l
    assert 10 not in l


def test_list_appends_x():
    l = LinkedList()
    l.append(1)
    l.append(2)
    l.append(3)
    assert len(l) == 3
    assert list(l) == [1, 2, 3]


def test_list_pops_item():
    l = LinkedList.fromvalues([1, 2, 3, 4, 5, 6])
    assert 1 == l.pop(0)
    assert len(l) == 5

    assert 6 == l.pop()
    assert len(l) == 4

    # [2, 3, 4, 5]
    assert 3 == l.pop(1)
    assert 4 == l.pop(-2)
    assert 5 == l.pop()
    assert 2 == l.pop()

    with pytest.raises(IndexError):
        l.pop()


def test_list_removes_x():
    l = LinkedList.fromvalues([1, 2, 3, 4, 5, 6])
    l.remove(1)
    assert 5 == len(l)
    assert 1 not in l

    with pytest.raises(ValueError):
        l.remove(10)


def test_list_indexes_x():
    l = LinkedList.fromvalues([1, 2, 3, 4, 5, 6])
    assert 0 == l.index(1)
    assert 5 == l.index(6)
    assert 5 == l.index(6, 5)

    with pytest.raises(ValueError):
        l.index(12)

    with pytest.raises(ValueError):
        l.index(1, 2)


def test_list_inserts_x():
    l = LinkedList.fromvalues([1])
    l.insert(0, 2)
    assert len(l) == 2
    assert [2, 1] == list(l)

    l.insert(3, 3)
    assert len(l) == 3
    assert [2, 1, 3] == list(l)

    l.insert(100, 100)
    assert [2, 1, 3, 100] == list(l)


@pytest.mark.parametrize('values, reversed_values',
                         [
                             ([1], [1]),
                             ([1, 2], [2, 1]),
                             ([1, 2, 3], [3, 2, 1]),
                         ])
def test_reverse_list(values, reversed_values):
    l = LinkedList.fromvalues(values)
    l.reverse()
    assert list(l) == reversed_values


def test_lists_are_equal():
    l1 = LinkedList.fromvalues([1, 2, 3, 4])

    with pytest.raises(TypeError):
        assert l1 == [1, 2, 3, 4]

    l2 = LinkedList.fromvalues([1, 2, 3])
    assert l1 != l2

    l3 = LinkedList.fromvalues([1, 2, 3, 4])
    assert l1 == l3
