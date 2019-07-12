# max heap
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

'''
# not verified version
def buildMaxHeap(arr):
    import math
    for i in range(math.floor(len(arr)/2),-1,-1):
        heapify(arr,i)

def heapify(arr, i):
    left = 2*i+1
    right = 2*i+2
    largest = i
    if left < arrLen and arr[left] > arr[largest]:
        largest = left
    if right < arrLen and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        swap(arr, i, largest)
        heapify(arr, largest)

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def heapSort(arr):
    global arrLen
    arrLen = len(arr)
    buildMaxHeap(arr)
    for i in range(len(arr)-1,0,-1):
        swap(arr,0,i)
        arrLen -=1
        heapify(arr, 0)
    return arr
'''