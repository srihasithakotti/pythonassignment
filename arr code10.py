def find_duplicates(arr):
    duplicates = []
    seen = {}

    for num in arr:
        if num in seen:
            if seen[num] == 1: 
                duplicates.append(num)
            seen[num] += 1
        else:
            seen[num] = 1

    return duplicates


arr = [10, 20, 30, 40, 50, 20, 10, 60, 30]
duplicates = find_duplicates(arr)
print("Duplicate values:", duplicates)