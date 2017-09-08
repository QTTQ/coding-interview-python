"""
    helpers
    ~~~~~~~~~~~~~~
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""
import random
from functools import wraps

__all__ = ('simple_cache', 'bubble_sort', 'insertion_sort',
           'selection_sort', 'merge_sort', 'quick_sort',
           'shell_sort', 'heap_sort')


#############################
# Bubble sort
# Time complexity:
#   - Best: O(n)
#   - Average: O(n^2)
#   - Worst: O(n^2)
# Space complexity: O(1)
# Stability: Yes
#############################

def bubble_sort(seq=None):
    if seq is None or len(seq) <= 1:
        return seq

    length = len(seq)
    for i in range(length):
        is_swapped = False
        # MIND HERE
        for j in range(length - 1, i, -1):
            if seq[j - 1] > seq[j]:
                is_swapped = True
                seq[j - 1], seq[j] = seq[j], seq[j - 1]

        if is_swapped is False:
            break

    return seq


#############################
# Selection sort
# Time complexity:
#   - Best: O(n^2)
#   - Average: O(n^2)
#   - Worst: O(n^2)
# Space complexity: O(1)
# Stability: Yes
#############################

def selection_sort(seq=None):
    if seq is None or len(seq) <= 1:
        return seq

    length = len(seq)
    for i in range(0, length):
        min_index = i

        # MIND HERE
        for j in range(i + 1, length):
            if seq[j] < seq[min_index]:
                min_index = j

        if i != min_index:
            seq[i], seq[min_index] = seq[min_index], seq[i]

    return seq


#############################
# Insertion sort
# Time complexity:
#   - Best: O(n)
#   - Average: O(n^2)
#   - Worst: O(n^2)
# Space complexity: O(1)
# Stability: Yes
#############################

def insertion_sort(seq=None):
    if seq is None or len(seq) <= 1:
        return seq

    length = len(seq)

    # MIND HERE: start with 1
    for i in range(1, length):
        val = seq[i]

        j = i
        while j > 0 and seq[j - 1] > val:
            seq[j] = seq[j - 1]
            j -= 1

        seq[j] = val

    return seq


#############################
# Shell sort
# Time complexity:
#   - Best: O(n log^2 n)
#   - Worst: O(n^2)
# Space complexity: O(1)
# Stability: No
#############################

def shell_sort(seq=None):
    if seq is None or len(seq) <= 1:
        return seq

    length = len(seq)
    gap = length // 2
    while gap > 0:
        # MIND HERE
        for i in range(gap, length):
            val = seq[i]
            j = i
            # MIND HERE: `j >= gap`
            while j >= gap and seq[j - gap] > val:
                seq[j] = seq[j - gap]
                j -= gap

            seq[j] = val

        gap //= 2

    return seq


#############################
# Merge sort
# Time complexity:
#   - Best: O(nlogn)
#   - Average: O(nlogn)
#   - Worst: O(nlogn)
# Space complexity: O(n)
# Stability: Yes
#############################

def merge_sort(seq=None):
    if seq is None or len(seq) <= 1:
        return seq

    def merge(left_, right_):
        from collections import deque
        merged, left_, right_ = deque(), deque(left_), deque(right_)
        while left_ and right_:
            merged.append(left_.popleft() if left_[0] < right_[0] else right_.popleft())
        merged.extend(left_ or right_)
        return list(merged)

    # MIND HERE
    mid = len(seq) // 2
    left = merge_sort(seq[:mid])
    right = merge_sort(seq[mid:])
    return merge(left, right)


#############################
# Heap sort
# Time complexity:
#   - Best: O(nlogn)
#   - Average: O(nlogn)
#   - Worst: O(nlogn)
# Space complexity: O(1)
# Stability: No
#############################

def heap_sort(seq=None):
    """Heap sort
    1. build heap
    2. swap with the element on the right side (keep bigger element on the right)
    3. rebuild heap(heapify)
    """
    if seq is None or len(seq) <= 1:
        return seq

    def heapify(seq, index, length):
        max_index = index
        left = index * 2 + 1
        right = index * 2 + 2
        if left < length and seq[left] > seq[max_index]:
            max_index = left
        if right < length and seq[right] > seq[max_index]:
            max_index = right

        if max_index != index:
            seq[index], seq[max_index] = seq[max_index], seq[index]
            heapify(seq, max_index, length)

    def build_heap(seq, length):
        # MIND HERE
        for j in range(length // 2, -1, -1):
            heapify(seq, j, length)

        return seq

    length_ = len(seq)
    seq = build_heap(seq, length_)

    # MIND HERE
    for i in range(length_ - 1, 0, -1):
        seq[0], seq[i] = seq[i], seq[0]
        heapify(seq, 0, i)

    return seq


#############################
# Quick sort
# Time complexity:
#   - Best: O(nlogn)
#   - Average: O(nlogn)
#   - Worst: O(n^2)
# Space complexity: O(logn) ~ O(n)
# Stability: No
#############################

def quick_sort(seq=None):
    """Quick sort
    1. choose a pivot
    1. make partition (left < pivot < right)
    """
    if seq is None or len(seq) <= 1:
        return seq

    def partition(left, right):
        pivot = random.randrange(left, right)
        pivot_value = seq[pivot]
        # MIND HERE
        seq[pivot], seq[right] = seq[right], seq[pivot]

        stored_index = left
        for i in range(left, right):
            # MIND HERE
            if seq[i] < pivot_value:
                seq[i], seq[stored_index] = seq[stored_index], seq[i]
                stored_index += 1

        seq[stored_index], seq[right] = seq[right], seq[stored_index]
        return stored_index

    def sort(left, right):
        if left < right:
            pivot = partition(left, right)
            sort(left, pivot - 1)
            sort(pivot + 1, right)

    sort(0, len(seq) - 1)
    return seq


#############################
# simple cache
#############################
def _make_key(args, kwargs):
    key = args

    for item in sorted(kwargs.items()):
        key += item

    return hash(key)


def simple_cache(func):
    cache = {}

    @wraps(func)
    def _(*args, **kwargs):
        key = _make_key(args, kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return _


if __name__ == '__main__':
    print(bubble_sort([3, 1, 0, 8]))
    print(selection_sort([3, 1, 0, 8]))
    print(insertion_sort([3, 1, 0, 8]))
    print(shell_sort([3, 1, 0, 8]))
    print(merge_sort([3, 1, 0, 8]))
    print(heap_sort([3, 1, 0, 8]))
    print(quick_sort([3, 0, 1, 8]))
