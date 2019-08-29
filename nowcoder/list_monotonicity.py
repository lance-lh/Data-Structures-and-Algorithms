def monotonicity(nums):
    return all(x < y for x,y in zip(nums,nums[1:])) \
        or all(x > y for x,y in zip(nums,nums[1:]))

a = [0,1,2,3,3,4] # This is a monotonically increasing list
b = [4.3,4.2,-2]  # This is a monotonically decreasing list
c = [2,3,1]       # This is neither
print(monotonicity(a))
print(monotonicity(b))
print(monotonicity(c))