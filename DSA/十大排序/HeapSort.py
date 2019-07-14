# max heap
'''
import heapq

def heapsort(arr):
    if not arr:
        return
    stack1 = []
    stack2 = []
    arr = [-i for i in arr]
    heapq.heapify(arr)
    print(arr)
    # for i in range(len(arr)):
    while len(arr):
        stack1.append(heapq.heappop(arr))
    while len(stack1):
        stack2.append(-stack1.pop())
    return stack2


if __name__ == "__main__":
    l = [1, 9, 2, 4, 7, 6, 3]
    print(heapsort(l))
'''

'''
# 寻找数组中最小的K个数,最大堆
import heapq
def heapsort(arr, k):
    heap = []
    length = len(arr)
    if not arr or k <= 0 or k > length:
        return
    k = k - 1
    for ele in arr:
        ele = -ele
        if len(heap) <= k:
            heapq.heappush(heap, ele)
        else:
            heapq.heappushpop(heap, ele)

    return map(lambda x:-x, heap)


if __name__ == "__main__":
    l = [1, 9, 2, 4, 7, 6, 3]
    min_k = heapsort(l, 3)
    print(list(min_k))
'''


# 1. build a max heap
def buildMaxHeap(arr):
    import math
    for i in range(math.floor(len(arr)/2),-1,-1):
        # derive their left and right child
        heapify(arr,i)

def heapify(arr, i):
    # left and right are i's child
    left = 2*i+1
    right = 2*i+2
    # record initial largest index as i
    largest = i

    # compare
    if left < arrLen and arr[left] > arr[largest]:
        largest = left
    if right < arrLen and arr[right] > arr[largest]:
        largest = right

    # if largest changes(not equal to i)
    if largest != i:
        # swap largest and i
        swap(arr, i, largest)
        # top to down heapify to rebuild a max heap
        heapify(arr, largest)

# swap to adjust
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def heapSort(arr):
    global arrLen
    arrLen = len(arr)
    # 1. build a max heap
    buildMaxHeap(arr)
    # after building a max heap
    for i in range(len(arr)-1,0,-1):
        # swap the head 0 with current i
        swap(arr,0,i)
        # decrease arr length
        arrLen -=1
        # rebuild max heap with array length minus 1
        heapify(arr, 0)
    return arr

if __name__ == "__main__":
    l = [1, 9, 2, 4, 7, 6, 3]
    print(heapSort(l))