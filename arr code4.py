def find_index(arr, element):
    try:
        return arr.index(element)
    except ValueError:
        return -1  
arr = [10, 20, 30, 40, 50]
element = 30
index = find_index(arr, element)

if index != -1:
    print(f"Element {element} found at index {index}")
else:
    print(f"Element {element} not found in the array")