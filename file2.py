file_path = 'output.txt'  

user_input = input("Please enter the text you want to write to the file: ")
try:
    with open(file_path, 'w') as file:
        file.write(user_input)  
    print(f"Text has been written to {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")