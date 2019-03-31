'''
2d array, every column and row ascend from little to big num
input a 2d array and an integer, judge if this integer included.
'''

# i starts from the leftmost row, and j starts from the rightmost column

def Find(target, array):
	if array == []:
		return False
		
    num_c = len(array[0])
    num_r = len(array)
	
    i = 0 # row
    j = num_c - 1   # column
    while i < num_r and j >= 0:
        if target < array[i][j]:
            j -= 1
        elif target > array[i][j]:
            i += 1
        else:
            return True


# test case
array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
target = 7
Find(target, array)
