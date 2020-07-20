def linear_search(arr, target):
    # Your code here
    # loop over every element in arr
    for i in range(len(arr)):
        # if element is equal to the target
        if arr[i] == target:
            # return the the element
            return i
    return -1   # target not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # set high point as the last element in array
    high = len(arr)-1 
    # set a low / middle point
    low = 0
    middle = 0
    # Your code here
    # create a while loop
    while high >= low:
        # find the middle point
        middle = (high + low // 2)
        # if middle point is less than target
        if arr[middle] < target:
            low = middle + 1 # ignore the left side of the arr
        # if middle point is higher than target
        elif arr[middle] > target:
            high = middle -1 # ignore the right side of the arr
        else:
            return middle
    return -1  # not found
