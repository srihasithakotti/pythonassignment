file_path = 'sample.txt'  


seek_position = 10

try:
    
    with open(file_path, 'r') as file:
        
        file.seek(seek_position)
        print(f"Moved to position {seek_position} in the file.")
        
    
        content = file.read()
        print("\nContent starting from position 10:")
        print(content)

except FileNotFoundError:
    print(f"The file at {file_path} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
