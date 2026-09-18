def calculate_grade(marks):
    average = sum(marks) / len(marks)

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "Fail"

    return average, grade


name = input("Enter student name: ")

marks = []

for i in range(3):
    mark = int(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)

average, grade = calculate_grade(marks)

print("\n--- Student Result ---")
print("Name:", name)
print("Marks:", marks)
print("Average:", average)
print("Grade:", grade)
