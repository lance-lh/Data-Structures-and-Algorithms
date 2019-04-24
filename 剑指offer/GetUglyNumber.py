'''
把只包含质因子2、3和5的数称作丑数（Ugly Number）。
例如6、8都是丑数，但14不是，因为它包含质因子7。
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
'''

'''
def GetUglyNumber(index):
    if index < 0:
        return 0
    num = 0
    uglyFound = 0
    while uglyFound < index:
        num += 1
        if IsUgly(num):
            uglyFound += 1
    return num


def IsUgly(num):
    while num % 2 == 0:
        num /= 2
    while num % 3 == 0:
        num /= 3
    while num % 5 == 0:
        num /= 5
    return True if num == 1 else False
'''

def GetUglyNumber(index):
    if index < 1:
        return 0

    res = [1]
    t2 = t3 = t5 = 0

    nextIndex = 1
    while nextIndex < index:
        # 每次添加最小的丑数到数列尾部
        minNum = min(res[t2] * 2, res[t3] * 3, res[t5] * 5)
        res.append(minNum)

        # 每次循环确保索引对应的值小于数列中的最大值
        while res[t2] * 2 <= minNum:
            t2 += 1
        while res[t3] * 3 <= minNum:
            t3 += 1
        while res[t5] * 5 <= minNum:
            t5 += 1

        nextIndex += 1

    return res[nextIndex - 1]

# test
index = 5
print(GetUglyNumber(index))