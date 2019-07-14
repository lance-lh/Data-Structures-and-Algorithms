# https://www.cnblogs.com/caseast/p/6085837.html
# https://github.com/hustcc/JS-Sorting-Algorithm/blob/master/1.bubbleSort.md

# complexity: O(n^2)
def bubblesort(arr):
    '''
    :param arr: list
    :return: list
    '''
    # i denotes each comparison, start from 1 to len
    # j denotes array index starting from 0 to len - i
    # inner loop depends on the current i
    for i in range(1, len(arr)):
        for j in range(0, len(arr) - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# test
a = [5, 2, 4, 3, 6, 8, 9, 7]
print(a)
print(bubblesort(a))