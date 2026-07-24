students = {
    "Tom": 70,
    "Jim": 80,
    "Sara": 90,
    "Liam": 85,
    "Kyle": 95
    }

total = 0
for score in students.values():
    total = total + score

average = total/len(students)
print("Class Average: ", average)

highest_student = max(students, key=students.get)
print("Top Student:", highest_student)
print("Highest Score:", students[highest_student])

lowest_student = min(students, key=students.get)
print("Bottom Student:", lowest_student)
print("Lowest Score:", students[lowest_student])

name = input("Enter student name: ")

if name in students:
    print(name, "Scored", students[name])
else:
    print("Student not found")