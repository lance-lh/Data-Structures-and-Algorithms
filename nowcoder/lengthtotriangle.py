zhouchang = int(input())
res = 0
for a in range(1,zhouchang//3):
    b = zhouchang - float(zhouchang) * zhouchang / (2*zhouchang - 2*a)
    b = float(b)
    if a < b and b - int(b) < 1e-5:
        res += 1
print(res)
