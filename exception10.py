def generate_class_not_found_exception():
    try:
        
        from non_existent_module import NonExistentClass
    except ImportError as e:
        
        print(f"ImportError: {e}")

def main():
    print("Attempting to generate ClassNotFoundException...")
    generate_class_not_found_exception()


main()