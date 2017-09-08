"""
    test_p07
    ~~~~~~~~~~~~~~

    Description of this module.
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

import pytest
from io import StringIO
from contextlib import redirect_stdout
from src.datastructures.linkedlist.single import List
from src.problems.p07_print_linkedlist_reversely import (visit_linkedlist_reversely1,
                                                         visit_linkedlist_reversely2)


@pytest.fixture(params=[visit_linkedlist_reversely2, visit_linkedlist_reversely1])
def visit_func(request):
    return request.param


@pytest.mark.parametrize('seq, expect',
                         [
                             ([], ''),
                             ([1], '1'),
                             ([1, 2, 3], '3 2 1'),
                             ([1, 0, 2], '2 0 1'),
                         ])
def test_visit_linkedlist_reversely(visit_func, seq, expect):
    assert visit_func(None) is None

    output = StringIO()
    with redirect_stdout(output):
        head = List.fromvalues(seq).head.next
        visit_func(head)

    assert output.getvalue().strip() == expect.strip()
