# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    length = len(arrA) + len(arrB)
    merged_arr = [0] * (length)
    a = 0
    b = 0
    m = 0
    while a < len(arrA) and b < len(arrB):
        if arrA[a] < arrB[b]:
            merged_arr[m] = arrA[a]
            a += 1
        elif arrA[a] >= arrB[b]:
            merged_arr[m] = arrB[b]
            b += 1
        m += 1
    while a < len(arrA):
        merged_arr[m] = arrA[a]
        a += 1
        m+= 1
    while b < len(arrB):
        merged_arr[m] = arrB[b]
        b += 1
        m += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    # print(left, right)
    arr = merge(left, right)
    return arr
arr = [4, 12, 43, 14, 56, 72, 19, 1]
print(merge_sort(arr))

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here

    pass