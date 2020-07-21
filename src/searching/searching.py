# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    start = 0
    end = (len(arr) -1)

    while start <= end:
        middle = (start + end)

        if arr[middle] == target:
            return middle
        else:
            if arr[middle] > target:
                end = middle - 1
            else:
                start = middle + 1
        
    return - 1





# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
#     # Your code here
#     pass

