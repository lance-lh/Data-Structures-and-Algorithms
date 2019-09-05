'''
题目：
    计算AUC

输入描述：
    第一行为输入的data行数N
    第二行开始为N行数据，每行形如1 0.95，即类别和预测分数

输出：
    AUC的值(格式化输出，保留两位小数)

测试用例：
    10
    1 0.90
    0 0.70
    1 0.60
    1 0.55
    0 0.52
    1 0.40
    0 0.38
    0 0.35
    1 0.31
    0 0.10
'''

# 以下两种解法，分别从库函数和auc意义出发解题
# 但是构造输入比较繁琐，为了直观表示，直接将输入格式调整好
# ref： https://blog.csdn.net/yinhui_zhang/article/details/96893330
# 示例及验证如下
def AUC(label, pre):
    # fill index in pos and neg
    pos = [i for i in range(len(label)) if label[i] == 1]
    neg = [i for i in range(len(label)) if label[i] == 0]

    # construct pos-neg pairs
    auc = 0
    for i in pos:
        for j in neg:
            if pre[i] > pre[j]:
                auc += 1
            elif pre[i] == pre[j]:
                auc += 0.5
            else:
                auc += 0

    return auc / (len(pos) * len(neg))

if __name__ == '__main__':
    label = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
    pre = [0.9, 0.7, 0.6, 0.55, 0.52, 0.4, 0.38, 0.35, 0.31, 0.1]
    print('my calculation:',AUC(label, pre))

    from sklearn.metrics import roc_curve,auc
    fpr, tpr, th = roc_curve(label, pre, pos_label=1)
    print('sklearn result', auc(fpr, tpr))



'''
# solution 1, sklearn function
import numpy as np
from sklearn.metrics import roc_auc_score

N = int(input())
tmp = []

for i in range(N):
    tmp.extend(input().split())

score = []
label = []
for i in range(len(tmp)):
    if i%2:
        score.append(float(tmp[i]))
    else:
        label.append(int(tmp[i]))

y = np.array(label)
x = np.array(score)
print('%.2f' %roc_auc_score(y,x))
'''

'''
# solution 2, auc formula
N = int(input())
tmp = []

for i in range(N):
    tmp.extend(input().split())
# print(tmp)

score = []
label = []
for i in range(len(tmp)):
    if i%2:
        score.append(float(tmp[i]))
    else:
        label.append(int(tmp[i]))
# print(score)
# print(label)

def auc(label,pre):
    pos = [i for i in range(len(label)) if label[i] == 1]
    neg = [i for i in range(len(label)) if label[i] == 0]
    auc = 0
    for i in pos:
        for j in neg:
            if pre[i] > pre[j]:
                auc += 1
            elif pre[i] == pre[j]:
                auc += 0.5
    return auc/(len(pos)*len(neg))

print('%.2f' %auc(label,score))
'''