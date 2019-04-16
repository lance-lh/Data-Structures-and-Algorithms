# https://github.com/hustcc/JS-Sorting-Algorithm/blob/master/5.mergeSort.md

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

def merge(left,right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result

# test
a = [5, 2, 4, 3, 6, 8, 9, 7]
print(a)
print(mergeSort(a))