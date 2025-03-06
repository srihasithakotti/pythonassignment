def second_largest(arr):
    if len(arr) < 2:
        return None  # Not enough elements

    arr = list(set(arr))  # Remove duplicates
    arr.sort(reverse=True)  # Sort in descending order
    return arr[1]  # Second largest element

# Example usage
arr = [10, 20, 30, 40, 50, 20, 10, 60, 30]
print("Second largest number:", second_largest(arr))