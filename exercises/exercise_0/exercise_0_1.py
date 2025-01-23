# 1. Schema validation

# from exercise_0_1d import validate_schema
#from timeit import timeit

#a)
student = {"id": 101, "name": "Erika", "is_active": True , "age": 45}

#b)
def validate_student(student):
    if not isinstance (student.get("id"), (int)):
        return False
    if not isinstance (student.get("name"), (str)):
        return False
    if not isinstance (student.get("is_active"), (bool)):
        return False
    if not isinstance (student.get("age"), (int)):
        return False
    
    # if all checks are passed, return True
    return True


#c)
# Create a list to store records
students = [
    {"id": 101, "name": "Erika", "is_active": True, "age": 45},
    {"id": 102, "name": "Marcus", "is_active": True, "age": 34},
    {"id": 103, "name": "David", "is_active": False, "age": 29},
    {"id": 104, "name": "Anna", "is_active": True, "age": 41.5},
    {"id": 106, "name": "Ingrid", "is_active": "NOPE", "age": 8},
 ]

# Validate each student and print the result
for student in students:
    is_valid = validate_student(student)
    print(f"Student {student['name']} is valid: {is_valid}")

# Check if all students are valid
is_all_valid = all(validate_student(student) for student in students)
print(f"All students valid: {is_all_valid}")

#d)
import jsonschema
from jsonschema import validate

# Define the JSON schema for a student record
student_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "is_active": {"type": "boolean"},
        "age": {"type": "number"}  # Allowing both integers and floats
    },
    "required": ["id", "name", "is_active", "age"]
}

# Sample student records (from your example)
students = [
    {"id": 102, "name": "Marcus", "is_active": True, "age": 34},
    {"id": 103, "name": "David", "is_active": False, "age": 29},
    {"id": 104, "name": "Anna", "is_active": True, "age": 41.5},
    {"id": 106, "name": "Ingrid", "is_active": "NOPE", "age": 8}  # Invalid
]

# Function to validate each student
def validate_student(student):
    try:
        validate(instance=student, schema=student_schema)
        return True  # Valid student
    except jsonschema.exceptions.ValidationError as ve:
        print(f"Validation error for {student['name']}: {ve.message}")
        return False  # Invalid student

# Validate each student
for student in students:
    is_valid = validate_student(student)
    print(f"Student {student['name']} is valid: {is_valid}")

# Check if all students are valid
is_all_valid = all(validate_student(student) for student in students)
print(f"All students valid: {is_all_valid}")

#e)

