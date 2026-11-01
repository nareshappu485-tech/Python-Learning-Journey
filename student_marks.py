students = {
    "Naresh": 85,
    "Kumar": 65,
    "Suresh": 30,
    "Ravi": 90
}

total = sum(students.values())
average = total / len(students)

print("STUDENT MARKS ANALYSIS")
print("----------------------")

for name, marks in students.items():
    status = "Pass" if marks >= 35 else "Fail"
    print(name, marks, status)

print("Total Marks:", total)
print("Average Marks:", average)
print("Highest Marks:", max(students.values()))
print("Lowest Marks:", min(students.values()))
