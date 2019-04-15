# https://github.com/hustcc/JS-Sorting-Algorithm/blob/master/3.insertionSort.md

# complexity: O(n^2)
def insertionsort(arr):
    '''
    :param arr: list
    :return: list
    '''
    for i in range(len(arr)):
        # note that preindex has left margin
        preindex = i - 1
        cur = arr[i]
        # find previous smallest array element
        while preindex >= 0 and cur < arr[preindex]:
            # if cur smaller than arr[preindex], move to the right
            arr[preindex+1] = arr[preindex]
            preindex -= 1
        # note while loop return smallest element (index - 1)
        arr[preindex+1] = cur
    return arr

# test
a = [5, 2, 4, 3, 6, 8, 9, 7]
print(a)
print(insertionsort(a))