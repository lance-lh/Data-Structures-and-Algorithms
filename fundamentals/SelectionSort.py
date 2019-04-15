# https://github.com/hustcc/JS-Sorting-Algorithm/blob/master/2.selectionSort.md

# complexity: O(n^2)
def selectionsort(arr):
    '''
    :param arr: list
    :return: list
    '''
    for i in range(len(arr) - 1):
        # 记录最小数的索引
        # 每次先把外循环索引作为当轮最小索引
        minIndex = i
        # 找到最小索引
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        # i 不是最小数时，将 i 和最小数进行交换
        # 注意不仅仅是将最小数赋给外循环索引位置，
        # 同时最小索引需要和外循环索引对应元素交换，以继续后续排序
        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr

# test
a = [5, 2, 4, 3, 6, 8, 9, 7]
print(a)
print(selectionsort(a))