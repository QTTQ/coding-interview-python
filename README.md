Coding Interview
------------------

[![Build Status](https://travis-ci.org/OxE8551CCB/coding-interview-python.svg)](https://travis-ci.org/OxE8551CCB/coding-interview-python) [![Coverage Status](https://coveralls.io/repos/github/OxE8551CCB/coding-interview-python/badge.svg?branch=master)](https://coveralls.io/github/OxE8551CCB/coding-interview-python?branch=master)

《剑指 Offer》中的面试题解决方案汇总，相关实现使用 Python 3.6 完成，使用 `pytest` 作为单元测试工具，`coverage` 提供测试覆盖率报告。

# 目录
## 数据结构
1. [栈](src/datastructures/stack.py)
1. [队列](src/datastructures/queue.py)
1. [双端队列](src/datastructures/deque.py)
1. [单向链表](src/datastructures/linkedlist/single.py)

## 排序算法
1. [冒泡排序：`bubble_sort`](src/helpers.py)
1. [选择排序：`selection_sort`](src/helpers.py)
1. [插入排序：`insertion_sort`](src/helpers.py)
1. [希尔排序：`shell_sort`](src/helpers.py)
1. [归并排序：`merge_sort`](src/helpers.py)
1. [堆排序：`heap_sort`](src/helpers.py)
1. [快速排序：`quick_sort`](src/helpers.py)

## 经典问题
1. [求链表中的倒数第 k 个节点](src/problems/p01_find_kth_node.py)
1. [找出数组中重复的数字](src/problems/p02_find_duplicate_numbers.py)
1. [不修改数组找出重复的数字](src/problems/p03_find_duplicate_numbers2.py)
1. [二维数组查找](src/problems/p04_find_in_sorted_matrix.py)
1. [字符串空格替换](src/problems/p05_replace_space_in_text.py)
1. [有序列表合并](src/problems/p06_merge_two_sorted_arrays.py)
1. [倒序打印链表](src/problems/p07_print_linkedlist_reversely.py)
1. [使用两个栈构建队列](src/problems/p08_impl_queue_with_two_stacks.py)
1. [使用两个队列构建栈](src/problems/p09_impl_stack_with_two_queues.py)
1. [计算斐波那契数列](src/problems/p10_fibonacci.py)
1. [员工年龄排序](src/problems/p11_sort_ages.py)
1. [旋转数组的最小数字](src/problems/p12_find_smallest_in_rotated_array.py)
1. [矩阵中的路径](src/problems/p13_matrix_has_path.py)
1. [机器人的活动范围](src/problems/p14_robot_range_of_motion.py)
1. [剪绳子](src/problems/p15_cut_rope.py)
1. [二进制中 1 的个数](src/problems/p16_number_of_one.py)
1. [数值的整数次方](src/problems/p17_power_of_n.py)
1. [删除链表的节点](src/problems/p18_delete_node_from_list.py)
1. [删除链表中重复的节点](src/problems/p19_remove_duplicate_nodes_from_list.py)
1. [正则表达式匹配](src/problems/p20_match_regex.py)
1. [调整数组顺序使奇数位于偶数前面](src/problems/p21_adjust_odd_even_nums_in_array.py)
1. [链表中环的入口节点](src/problems/p22_find_entry_of_partial_circular_list.py)
1. [链表反转](src/problems/p23_reverse_list.py)
1. [合并两个排序链表](src/problems/p24_merge_sorted_list.py)