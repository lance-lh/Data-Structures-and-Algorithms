# https://github.com/hustcc/JS-Sorting-Algorithm/blob/master/5.mergeSort.md
# https://www.cnblogs.com/chengxiao/p/6194356.html

# complexity: O(nlogn)
def mergeSort(arr):
    '''
    :param arr: list
    :return: list
    '''
    if(len(arr)<2):
        return arr
    middle = len(arr)//2
    left, right = arr[0:middle], arr[middle:]
    return merge(mergeSort(left), mergeSort(right))
    # after this, divide arr into each seperate num and it looks like a binary tree with log n depth.

# then conquer, it needs n steps
# so complexity is O(nlogn)
def merge(left,right):
    # space for time
    result = []
    # compare left and right elements, add it to the res
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    # if right branch is empty, add the left elements into the end of res
    while left:
        result.append(left.pop(0))
    # if left branch is empty, add the right elements into the end of res
    while right:
        result.append(right.pop(0))
    return result

# test
a = [5, 2, 4, 3, 6, 8, 9, 7]
print(a)
print(mergeSort(a))
