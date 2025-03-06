def remove_element(arr, element):
    if element in arr:
        arr.remove(element)  
    else:
        print(f"{element} not found in the array")
    return arr