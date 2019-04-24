#coding:utf-8
'''
find a first character in string
return its location
if not exist, return -1
capital case and little case differ
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
    # char has 8 bits, therefore 2^8 possibilities
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
