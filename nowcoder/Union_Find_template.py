'''
三步走：
1.  初始化pre和ranks数组，pre为每个元素的父结点（上一级），
    ranks为每个元素作为根节点时的树的秩（树的深度），
    一开始设置pre的每个值为每个元素自己，设置ranks每个值为0.
2.  find() 查询该元素的首级，顺便做路径压缩
3.  join() 合并两个集合，按秩合并，秩小的树的根节点指向秩大的树的根节点。
————————————————
原文链接：https://blog.csdn.net/AivenZhong/article/details/89148862
'''

def find(x, pre):
    """
    查找x的最上级（首级）
    :param x: 要查找的数
    :param pre: 每个元素的首级
    :return: 元素的上一级
    """
    # root:根节点， p:指针
    root, p = x, x

    # 找根节点
    while root != pre[root]:
        root = pre[root]

    # 路径压缩，把每个经过的结点的上一级设为root（直接设为首级）
    while p != pre[p]:
        p, pre[p] = pre[p], root
    return root


def join(x, y, pre, ranks):
    """
    合并两个元素（合并两个集合）
    :param x: 第一个元素
    :param y: 第二个元素
    :param pre: 每个元素的上一级
    :param ranks: 每个元素作为根节点时的秩（树的深度）
    :return: None
    """
    h1, h2 = find(x, pre), find(y, pre)
    # 当两个元素不是同一组的时候才合并
    # 按秩合并
    # 秩小的附属于秩大的（成本低）
    if h1 != h2:
        if ranks[h1] < ranks[h2]:
            pre[h1] = h2
        # if ranks(h1) >= ranks(h2)
        # here, two conditions are included
        else:
            pre[h2] = h1
            if ranks[h1] == ranks[h2]:
                ranks[h1] += 1


# 结点数
n = 10

# 边数据
data = [[0, 9], [9, 3], [1, 2], [2, 8], [4, 5], [6, 7], [0, 5], [6, 8]]

# pre一开始设置每个元素的上一级是自己，ranks一开始设置每个元素的秩为0
pre, ranks = [i for i in range(n)], [0] * n

for edge in data:
    join(edge[0], edge[1], pre, ranks)

print('pre:\t', pre)
print('ranks:\t', ranks)
print('idx:\t', list(range(n)))

# pre:	 [0, 6, 1, 0, 0, 4, 6, 6, 1, 0]
# ranks:	 [2, 1, 0, 0, 1, 0, 2, 0, 0, 0]
# idx:	 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
