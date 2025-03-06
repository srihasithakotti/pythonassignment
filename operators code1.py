def arithmetic_operations(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    if num2 != 0:
        division = num1 / num2
    else:
        division = "Cannot divide by zero"
    return {
        "addition": addition,
        "subtraction": subtraction,
        "multiplication": multiplication,
        "division": division
    }