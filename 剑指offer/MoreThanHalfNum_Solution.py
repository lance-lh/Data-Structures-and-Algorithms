'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
    例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
    由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。
如果不存在则输出0。
'''


# note:题目最后返回为一个整型

def MoreThanHalfNum_Solution(numbers):
    '''
    :param numbers: list
    :return: int
    '''
    d = {}
    res = 0

    for k, v in enumerate(numbers):
        if v in d:
            d[v] += 1
        else:
            d[v] = 1

    for i in d:
        if d[i] > len(numbers) // 2:
            res = i
    return res


# test
num = [1,2,3,2,2,2,5,4,2]
print(MoreThanHalfNum_Solution(num))