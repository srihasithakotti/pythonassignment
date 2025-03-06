def average_array(arr):
    if len(arr) == 0:
        return 0  
    
    total = sum(arr)  
    count = len(arr)  
    average = total / count  
    return average