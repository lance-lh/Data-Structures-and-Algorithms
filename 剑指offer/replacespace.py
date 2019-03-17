'''
substitute space with “%20”
'''

def replaceSpace(s):

    # check boundary
    if not isinstance(s, str) or len(s) <= 0 or s == None:
        return ''

    # count space num
    cnt = 0
    for c in s:
        if c == ' ':
            cnt += 1

    # new string setting
    oldstrlen = len(s)
    newstrlen = oldstrlen + 2 * cnt
    newstr = [None] * newstrlen
    newstrindex = newstrlen - 1
    oldstrindex = oldstrlen - 1

    # substitute, whether space or not
    while newstrindex >= oldstrindex and newstrindex >= 0:
        if s[oldstrindex] == ' ':
            newstr[newstrindex - 2 : newstrindex + 1] = ['%','2','0']
            newstrindex -= 3
            oldstrindex -= 1
        else:
            newstr[newstrindex] = s[oldstrindex]
            newstrindex -= 1
            oldstrindex -= 1
    return ''.join(newstr)

# test
# s = 'We Are Happy'
s = 'helloworld '
print(s)
print(replaceSpace(s))