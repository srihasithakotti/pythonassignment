def is_palindrome(value):
    value_str = str(value)  
    return value_str == value_str[::-1] 


value = input("Enter a number or string: ")


if is_palindrome(value):
    print(f"{value} is a Palindrome.")
else:
    print(f"{value} is not a Palindrome.")