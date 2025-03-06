def max_min_difference(arr):
    if not arr:  
        return None  

    return max(arr) - min(arr)


arr = [10, 20, 30, 40, 50, 5, 60]
print("Difference between largest and smallest value:", max_min_difference(arr))