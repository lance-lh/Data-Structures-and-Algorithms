'''
删除字符串中出现次数最少的字符，
返回与原字符串顺序一致的删除后字符串
'''
while True:
    try:
        strin=input()

        d=[] # d stores char counts
        l=[] # l stores str after deleting
        for i in strin:
            d.append(strin.count(i))
        m=min(d)
        for i in range(len(d)):
            if d[i]!=m:
                l.append(strin[i])
        res=''.join(map(str,l))
        print(res)

    except:
        break

# test
# abcab