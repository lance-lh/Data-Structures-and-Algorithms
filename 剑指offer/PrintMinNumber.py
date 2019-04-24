'''
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，
打印能拼接出的所有数字中最小的一个。
    例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
'''

def PrintMinNumber(numbers):
    if not numbers:
        return ""
    ss = [str(i) for i in numbers]

    return int(min(Permutation(ss)))

def Permutation(ss):

    if len(ss) <= 1:
        return ss
    res = []

    for i in range(len(ss)):
        for j in Permutation(ss[:i] + ss[i + 1:]):
            #if j not in res:
            res.append(ss[i] + j)
    return res

# test
numbers = [3,1,2,5,4]
print(PrintMinNumber(numbers))