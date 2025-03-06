def is_armstrong(number):
    num_str = str(number)  
    num_length = len(num_str)  
    armstrong_sum = sum(int(digit) ** num_length for digit in num_str)  

    return armstrong_sum == number 


num = int(input("Enter a number: "))


if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")