import time
'''
# solution 1
# Time costs: 0.2028806209564209
ts = time.time()
zc = 120
res = 0
for i in range(1,zc):
    for j in range(1,zc):
        for k in range(1,zc):
            if i+j+k == zc and i*i+j*j == k*k:
                res += 1
print(res//2)
te = time.time()
print("Time costs:",te - ts)
'''

'''
# solution 2
# Time costs: 0.0019986629486083984
ts = time.time()
zc = 120
res = 0
for i in range(1,zc):
    for j in range(i,zc):
        k = zc - i - j
        if i*i+j*j == k*k:
            res += 1
print(res)
te = time.time()
print("Time costs:",te - ts)
'''

'''
# solution 3
# Time costs: 0.00099945068359375
ts = time.time()
zc = 120
res = 0
for i in range(1,zc//3):
    for j in range(i,zc//2):
        k = zc - i - j
        if i*i+j*j == k*k:
            res += 1
print(res)
te = time.time()
print("Time costs:",te - ts)
'''

'''
# solution 4
# Time costs: 0.0009992122650146484
ts = time.time()
zc = 120
res = 0
for i in range(1,zc//3):
    for j in range(i,zc//2):
        k = zc - i - j
        if i*i+j*j == k*k and k < i+j:
            res += 1
print(res)
te = time.time()
print("Time costs:",te - ts)
'''


# '''
zc = int(input())
ts = time.time()
res = 0
for i in range(1,zc//3):
    j = zc - float(zc) * zc / (2*zc - 2*i)
    j = float(j)
    if i < j and j - int(j) < 1e-5:
        res += 1
print(res)
te = time.time()
print("Time costs:",te - ts)
# '''