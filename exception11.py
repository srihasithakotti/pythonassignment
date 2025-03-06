def generate_io_exception():
    try:
    
        with open('/non_existent_directory/non_existent_file.txt', 'r') as file:
            content = file.read()
            print(content)
    except IOError as e:

        print(f"IOError: {e}")


def main():
    print("Attempting to generate IOError...")
    generate_io_exception()

main()