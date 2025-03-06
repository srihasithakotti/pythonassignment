def remove_duplicates(arr):
    seen = set()
    unique_arr = []
    
    for num in arr:
        if num not in seen:
            unique_arr.append(num)
            seen.add(num)
    
    return unique_arr

arr = [10, 20, 30, 40, 50, 20, 10, 60, 30]
unique_arr = remove_duplicates(arr)
print("Array after removing duplicates:", unique_arr)