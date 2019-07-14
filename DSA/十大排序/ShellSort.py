# https://github.com/MisterBooo/Article

# 基于希尔排序，从后往前查找时，从-1变为-gap
# 设数组长度为n，则gap为n//3 + 1(向下取整加1)
# 之后循环， gap = gap//3 (自身向下取整)

# complexity: O(nlogn)
def shellsort(arr):
    '''
    :param arr: list
    :return: list
    '''
    gap = 1
    # gap为数组长度向下取3整加1
    while gap < len(arr) / 3:
        gap = gap * 3 + 1
    while gap > 0:
        for i in range(gap, len(arr)):
            preindex = i - gap
            cur = arr[i]

            while preindex >= 0 and cur < arr[preindex]:
                arr[preindex+gap] = arr[preindex]
                preindex -= gap
            arr[preindex+gap] = cur
        gap = gap // 3
    return arr

# test
a = [5, 2, 4, 3, 6, 8, 9, 7]
print(a)
print(shellsort(a))