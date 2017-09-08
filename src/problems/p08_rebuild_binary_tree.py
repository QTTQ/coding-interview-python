"""
    p08_rebuild_binary_tree
    ~~~~~~~~~~~~~~

    输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序
    遍历的结果中都不包含重复的数字。
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""


class BinaryTreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


if __name__ == '__main__':
    pass
