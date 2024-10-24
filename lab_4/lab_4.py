# Initial Dictionary of Students
students = [
    {
        "name": "Matt Donohue",
        "major": "Cybersecurity",
        "grade": 12,
        "gpa": 4.0
    }
]

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

        new_student[key] = value

    students.append(new_student)

    repeat = input("\tAdd another student? Y/n: ")
    if repeat.lower() != "y":
        break

# 4. Printing the Roster
print(students)
print("==========")
for student in students:
    for key, value in student.items():
        if key == "grade":
            if value == 9:
                print(f"{key.capitalize()}: Freshman")
            elif value == 10:
                print(f"{key.capitalize()}: Sophomore")
            elif value == 11:
                print(f"{key.capitalize()}: Junior")
            elif value == 12:
                print(f"{key.capitalize()}: Senior")
        else:
            print(f"{key.capitalize()}: {value}")
    
    print("==========")

