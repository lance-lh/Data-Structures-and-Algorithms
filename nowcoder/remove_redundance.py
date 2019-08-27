
# solution 1
a = [1,2,1,3,4,5,5]

a = list(set(a))
print(a)

# solution 2
a = [1,2,1,3,4,5,5]

res = []
for i in a:
    if i not in res:
        res.append(i)
print(res)
