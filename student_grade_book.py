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

highest = max(students.values())
