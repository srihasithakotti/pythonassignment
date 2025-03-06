def generate_file_not_found_exception():
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
        print(content)

def main():
    try:
        generate_file_not_found_exception() 
    except FileNotFoundError as e:
    
        print(f"FileNotFoundError: {e}")

main()