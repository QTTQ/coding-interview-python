"""
    module single
    ~~~~~~~~~~~~~~

    Singly linked list.

     ---------
    |data|next| -> ...
     ---------

    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""


class Node(object):
    __slots__ = 'val', 'next'

    def __init__(self, val, next_):
        self.val = val
        self.next = next_

    def __repr__(self):
        return 'Node({!r})'.format(self.val)


class List(object):
    def __init__(self):
        # make an empty node as the root node.
        # the size of the list can be stored in the empty node.
        self._root = Node(0, None)

    @property
    def head(self):
        return self._root

    @classmethod
    def fromhead(cls, head):
        o = cls()
        o._root = head
        return o

    @classmethod
    def fromvalues(cls, values=None):
        """Create a linked-list from an iterable object, e.g `list`
        """
        o = cls()

        for v in values:
            o.append(v)

        return o

    def append(self, x):
        self.insert(len(self), x)

    def pop(self, index=-1):
        x = self[index]
        self.remove(x)
        return x

    def clear(self):
        p = self._root.next
        while p:
            old = p
            p = p.next
            del old

        self._root = Node(0, None)

    def remove(self, x):
        cur = self._root.next
        prior = self._root

        while cur:
            if cur.val == x:
                prior.next = cur.next
                # decrease the list size
                self._root.val -= 1
                del cur
                break

            prior = cur
            cur = cur.next
        else:
            raise ValueError('{} not in list'.format(x))

    def index(self, x, start=None, stop=None):
        start = start or 0
        stop = stop or len(self)
        for i, v in enumerate(self):
            if start <= i < stop:
                if x == v:
                    return i
        else:
            raise ValueError('{} is not in the list'.format(x))

    def insert(self, index, x):
        cur = self._root.next
        prior = self._root
        i = 0

        while cur:
            if index == i or i >= len(self):
                break

            prior = cur
            cur = cur.next
            i += 1

        node = Node(x, cur)
        prior.next = node
        # increase list size
        self._root.val += 1

    def reverse(self):
        if len(self) == 1:
            return

        prior = self._root.next
        cur = prior.next
        prior.next = None

        while cur:
            # point to the prior node
            next_node = cur.next
            cur.next = prior

            prior = cur
            cur = next_node
        else:
            self._root.next = prior

    def find_node(self, val):
        p = self._root.next
        while p and p.val != val:
            p = p.next

        return p

    def __len__(self):
        return self._root.val

    def __iter__(self):
        p = self._root.next
        while p:
            yield p.val
            p = p.next

    def __getitem__(self, item):
        item_ = item if item >= 0 else len(self) + item
        for i, x in enumerate(self):
            if item_ == i:
                return x
        else:
            raise IndexError('index {} is out of range'.format(item))

    def __str__(self):
        return '[{}]'.format(', '.join(map(str, self)))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError('{!r} is not of type {}'.format(other, self.__class__.__name__))

        if len(self) != len(other):
            return False

        for a, b in zip(self, other):
            if a != b:
                return False

        return True


if __name__ == '__main__':
    l = List.fromvalues([1, 2, 4, 5])
    print(l)
    print(len(l))
    print(2 in l)

    l.remove(5)
    print(l)

    # print(l[8])

    l.insert(1000, 100)
    print(l)

    l.reverse()
    print(l)
