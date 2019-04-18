
def convert(s, numRows):
    '''
    :param s:str
    :param numRows: int
    :return: str
    '''
    # Corner Case
    if numRows == 1 or numRows >= len(s):
        return s

    # Create an array of strings for all n rows
    arr = ["" for x in range(numRows)]

    # Initialize index for array of strings arr[]
    row = 0

    # Travers through given string
    for i in range(len(s)):

        # append current character to current row
        arr[row] += s[i]

        # If last row is reached, change direction to 'up'
        if row == numRows - 1:
            down = False

        # If 1st row is reached, change direction to 'down'
        elif row == 0:
            down = True

        # If direction is down, increment, else decrement
        if down:
            row += 1
        else:
            row -= 1

    return ''.join(arr)

# test
s = "PAYPALISHIRING"
numRows = 4
print(convert(s, numRows))