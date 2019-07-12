def countsort(arr):
    maxval = max(arr)
    bucketLen = maxval+1 # index from 0
    bucket = [0]*bucketLen
    ind = 0
    arrLen = len(arr)

    for i in range(arrLen):
        bucket[arr[i]]+=1

    for j in range(bucketLen):
        while bucket[j] > 0:
            arr[ind] = j
            ind += 1
            bucket[j] -= 1
    return arr

if __name__ == "__main__":
    l = [1, 9, 2, 4, 7, 6, 3]
    print(countsort(l))