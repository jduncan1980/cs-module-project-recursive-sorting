# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, min, max):
    if max >= min:
        # min = 0
        # max = len(arr) - 1
            
        mid = (min + max) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr, target, min, mid-1)
        elif arr[mid] < target:
            return binary_search(arr, target, mid+1, max)
    else:   
        return -1

arrA = [1, 4, 5, 9, 12, 16, 22]
print(binary_search(arrA, 5, 0, len(arrA)-1))


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
