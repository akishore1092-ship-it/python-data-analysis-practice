# Lists and Dictionaries - Data Analysis Practice

# A list of marks
marks = [78, 85, 92, 67, 88]

print("Marks:", marks)
print("First mark:", marks[0])
print("Number of marks:", len(marks))

# Calculate total and average
total = sum(marks)
average = total / len(marks)

print("Total:", total)
print("Average:", average)

# A dictionary containing student information
student = {
    "name": "Kishore",
    "course": "MSc Applied Data Science",
    "age": 22
}

print("Student name:", student["name"])
print("Course:", student["course"])

# Loop through the marks
print("All marks:")

for mark in marks:
    print(mark)

