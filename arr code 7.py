def insert_element(arr, element, position):
    
    if position < 0 or position > len(arr):
        print("Invalid position")
        return arr
    
    arr.insert(position, element) 
    return arr