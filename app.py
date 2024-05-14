def format_student_data(students):
    formatted_data = []
    for key, value in students.items():
        name = value['name']
        age = value['details']['age']
        brgy = value['details']['brgy']
        formatted_data.append(f"Key: {key}, Name: {name}, Age: {age}, Barangay: {brgy}")
    return "\n".join(formatted_data)

students = {
    8: {'name': 'JOE', 'details': {'age': 19, 'brgy': 'Fairview'}, 'subject': {'DASTRUC': [2.0, 4.0, 3.0]}},
    6: {'name': 'KYL', 'details': {'age': 22, 'brgy': 'Maligaya'}, 'subject': {'DASTRUC': [2.0, 4.0, 1.0]}},
    3: {'name': 'CHA', 'details': {'age': 26, 'brgy': 'Fairview'}, 'subject': {'DASTRUC': [1.0, 2.0, 4.0]}},
    1: {'name': 'PAT', 'details': {'age': 28, 'brgy': 'Maligaya'}, 'subject': {'DASTRUC': [3.5, 2.0, 4.0]}},
    4: {'name': 'TAP', 'details': {'age': 21, 'brgy': 'Fairview'}, 'subject': {'DASTRUC': [2.5, 2.0, 1.5]}},
    5: {'name': 'CAT', 'details': {'age': 23, 'brgy': 'Maligaya'}, 'subject': {'DASTRUC': [1.5, 4.0, 3.0]}},
}

sorted_students = {k: students[k] for k in sorted(students.keys())}

print(format_student_data(sorted_students))