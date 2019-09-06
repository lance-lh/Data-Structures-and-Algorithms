def permutation(a,b):
    from collections import defaultdict
    res = []
    c = [''.join(sorted(i)) for i in b]
    d = defaultdict(list)
    # d = {}
    for k,v in enumerate(c):
        # if v not in d:
        #     d[v] = []
        d[v].append(b[k])
    for i in d:
        if len(d[i]) > 1:
            res.append(d[i])
    return res

if __name__ == '__main__':
    # a = 4
    # b = ['abcd','sdfg','gsfd','bcda']
    a = 7
    b = ['abcd','zesa','saze','abc','pqrst','cdab','bacd']
    print(permutation(a,b))