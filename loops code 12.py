def print_gender(gender):
    switch = {
        'M': "Male",   
        'F': "Female"  
    }

    return switch.get(gender.upper(), "Invalid input")  

gender_input = input("Enter M for Male or F for Female: ")