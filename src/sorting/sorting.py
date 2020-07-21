# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements

    # Your code here
    result = []
    left = 0 
    right = 0

    while left < len(arrA) and right < len(arrB):
        if arrA[left] < arrB[right]:
            result.append(arrA[left])
            left += 1
        else: 
            result.append(arrB[right])
            right += 1
    result += arrA[left:]
    result += arrB[right:]

    return result


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2

    left_sequence = merge_sort(arr[:mid])
    right_sequence = merge_sort(arr[mid:])

    arr = merge(left_sequence, right_sequence)
        
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

