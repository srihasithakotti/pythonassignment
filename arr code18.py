def remove_duplicates(arr):
    seen = set()
    unique_arr = []

    for num in arr:
        if num not in seen:
            unique_arr.append(num)
            seen.add(num)
    
    return unique_arr

# Example usage
arr = [10, 20, 30, 40, 50, 20, 10, 60, 30]
new_arr = remove_duplicates(arr)
print("Array after removing duplicates:", new_arr)