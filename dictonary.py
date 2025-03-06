# 1.1 Creating a dictionary with at least 5 key-value pairs (Student ID and Name)
students = {
    101: "John Doe",
    102: "Jane Smith",
    103: "Alice Brown",
    104: "Bob Johnson",
    105: "Charlie Davis"
}

# 1.2 Adding values to the dictionary
# Adding a new student entry to the dictionary
students[106] = "David Wilson"
print("After Adding a New Student:")
print(students)

# 1.3 Updating values in the dictionary
# Updating the name of the student with ID 103
students[103] = "Alicia Brown"
print("\nAfter Updating Student Name with ID 103:")
print(students)

# 1.4 Accessing a value in the dictionary
# Accessing the name of the student with ID 102
student_name = students.get(102)  # Using the get method
print("\nAccessed Student with ID 102:", student_name)

# 1.5 Create a nested loop dictionary (A dictionary with student details as nested dictionaries)
nested_students = {
    101: {"name": "John Doe", "age": 20, "course": "Math"},
    102: {"name": "Jane Smith", "age": 22, "course": "Science"},
    103: {"name": "Alice Brown", "age": 21, "course": "History"},
    104: {"name": "Bob Johnson", "age": 23, "course": "Engineering"},
    105: {"name": "Charlie Davis", "age": 24, "course": "Literature"}
}

# 1.6 Access the values of the nested dictionary (nested loop for accessing each student’s data)
print("\nAccessing Nested Dictionary:")
for student_id, details in nested_students.items():
    print(f"Student ID {student_id}: Name = {details['name']}, Age = {details['age']}, Course = {details['course']}")

# 1.7 Print the keys present in a particular dictionary
print("\nKeys present in the students dictionary:")
print(students.keys())

# 1.8 Delete a value from a dictionary
# Deleting the student with ID 105 from the dictionary
del students[105]
print("\nAfter Deleting Student with ID 105:")
print(students)