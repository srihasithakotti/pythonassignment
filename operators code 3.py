def check_equal(num1, num2):
    if num1 == num2:
        return "The numbers are equal."
    else:
        return "The numbers are not equal."
        
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = check_equal(num1, num2)
print(result)