# School Example
students = {
    'student1': {'name': 'Alice', 'age': 15, 'grade': '9th'},
    'student2': {'name': 'Bob', 'age': 14, 'grade': '8th'},
    'student3': {'name': 'Charlie', 'age': 16, 'grade': '10th'}
}

# Accessing information about a student
student_id = 'student2'
student_info = students.get(student_id, 'Student not found')
print(f"Student Information for {student_id}: {student_info}")