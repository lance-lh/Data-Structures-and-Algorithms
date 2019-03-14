#coding:utf-8
'''
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中
找到第一个只出现一次的字符,并返回它的位置,
如果没有则返回 -1（需要区分大小写）.
'''

# method 1
'''
def FirstNotRepeatingChar(s):
    # check conditions
    if len(s) <= 0 or len(s) >= 10000:
        return -1

    for i in s:
        if s.count(i) == 1: # count() indicates a loop
            return s.index(i)  # string method
'''

# hash table
# using two hash table
# one to traverse, to store key: character, value as count
# the other one to find first value = 1
# O(n)

def FirstNotRepeatingChar(s):
    lst = [0] * 256 # [0] * 256 is accurate
    if len(s) <= 0 or len(s) >= 10000:
        return -1

    for c in s:
        # ord to convert character to ascii
        lst[ord(c)] += 1

    for i in s:
        if lst[ord(i)] == 1:
            return s.index(i)
            break
    return -1

#test
s = 'ssfdjleo'
ans = FirstNotRepeatingChar(s)
print(ans)
