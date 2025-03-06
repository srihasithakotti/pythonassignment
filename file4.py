file_path = 'sample.txt' 

try:

    with open(file_path, 'r') as file:
        
        print("Reading the first 10 bytes:")
        content = file.read(10)
        print(content)  
        
        
        file.seek(5) 
        print("\nReading 10 bytes starting from position 5:")
        content = file.read(10)
        print(content)  
        
    
        print("\nCurrent file pointer position:", file.tell())
        
    
        file.seek(0, 2) 
        print("\nReading the last 10 bytes:")
        content = file.read(10)
        print(content)  

except FileNotFoundError:
    print(f"The file at {file_path} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")


