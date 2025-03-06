def find_common_elements(arr1, arr2):
    
    common_elements = set(arr1) & set(arr2)
    return list(common_elements)