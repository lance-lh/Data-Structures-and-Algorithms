# https://blog.csdn.net/adusts/article/details/80882649
# https://github.com/qiwsir/algorithm/blob/master/quick_sort.md
# https://github.com/hustcc/JS-Sorting-Algorithm/blob/master/6.quickSort.md

# complexity: O(nlogn)
def quicksort(arr):
    '''
    :param arr: list
    :return: list
    '''
    if not arr:
        return []
    else:
        pivot = arr[0]
        left = [x for x in arr if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)

# test
a = [5,1,2,9,3,6,4,7,10,8]
print(a)
print(quicksort(a))