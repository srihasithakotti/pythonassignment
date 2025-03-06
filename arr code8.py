def find_min_max(arr):
    if not arr: 
        return None, None
    return min(arr), max(arr)


arr = [10, 20, 5, 40, 50]
minimum, maximum = find_min_max(arr)

print(f"Minimum value: {minimum}")
print(f"Maximum value: {maximum}")