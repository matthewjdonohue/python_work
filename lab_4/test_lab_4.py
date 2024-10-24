# Initial Dictionary of Students
students = [
    {
        "name": "Matt Donohue",
        "major": "Cybersecurity",
        "grade": 9,
        "gpa": 4.0
    }
]

# Getting grade names
def get_student_grade(grade):
    grade_names = {
        9: "Freshman",
        10: "Sophomore",
        11: "Junior",
        12: "Senior"
    }
    return grade_names

for student in students:
    student["grade"] = get_student_grade(student["grade"])

# 3. User Input
while True: 
    print("Creating new student. Please fill out requested info.")
    new_student = {}

    while True:
        key = input("\tEnter new key for student, or 'q' to finish creating new student: ")
        if key.lower() == "q":
            break
        value = input("\tEnter new value for student, or 'q' to finish creating new student: ")
        if value.lower() == "q":
            break

        if value.isdigit():
            value = int(value)
        else:
            try:
                value = float(value)
            except ValueError:
                pass

        if key == "grade":
            value = get_student_grade(value)
            
        new_student[key] = value

    students.append(new_student)

    repeat = input("\tAdd another student? Y/n: ")
    if repeat.lower() != "y":
        break

# 4. Printing the Roster
print("\nStudent Roster:")
for student in students:
    for key, value in student.items():
        print(f"{key.capitalize()}: {value}")
    print()
