# Input marks from the user
marks = float(input("Enter the student's marks: "))

# Determine the grade based on the given scheme
if 90 <= marks <= 100:
    grade = 'Ex'
elif 80 <= marks < 90:
    grade = 'A'
elif 70 <= marks < 80:
    grade = 'B'
elif 60 <= marks < 70:
    grade = 'C'
elif 50 <= marks < 60:
    grade = 'D'
elif marks < 50:
    grade = 'F'
else:
    grade = 'Invalid marks'

# Print the result
print(f"The student's grade is: {grade}")
