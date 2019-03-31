'''
In computer memory, there are two byte-orders, they are: big-endian and little-endian.
big endian indicates placing high-order bytes in low addr,
while little indicates placing high-order bytes in high addr, which matches human cognition.

Now define a new character encoding mode:
    9 characters form a group
    first char：　0 indicates little endian, 1 big endian.

U need to input a number and a string includes 9 numbers.
according to the order that several encoding groups appear,
print the results in one line separated with space,
and no newline ends.

e.g.
    2
    0ajklkshl1kdbaslsi

    result:
        lhsklkja kdbaslsi
'''

def ToBigEndian(N, s):
    '''
    :param N: int
    :param string: str
    :return: str
    '''

    # check
    # if not isinstance(s, str) or len(s)%9 != 0 or s == None or N < 0:
    #     return ''

    res = ''
    for i in range(N):
        # flag indicates nums leading the next 8 characters
        flag = int(s[9*i])

        # 0, reverse the string
        if flag == 0:
            res += s[1+9*i:9+9*i][::-1]
            res += ' '
        # 1, just add string to the string
        else:
            res += s[1+9*i:9+9*i]
            res += ' '
    return res


#test
print(ToBigEndian(2,'0ajklkshl1kdbaslsi'))
print(ToBigEndian(3,'0ajklkshl1kdbaslsi0jckoxdsk'))
