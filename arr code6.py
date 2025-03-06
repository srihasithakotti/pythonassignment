def copy_array(arr):
    return arr.copy()

arr1 = [10, 20, 30, 40, 50]
arr2 = copy_array(arr1)

print("Original Array:", arr1)
print("Copied Array:", arr2)