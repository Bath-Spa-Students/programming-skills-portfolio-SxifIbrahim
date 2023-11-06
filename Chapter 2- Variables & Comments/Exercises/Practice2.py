"""
Write a python program that takes courses marks as input and then calculates average of all the
courses. After calculating the average, calculate the percentage of a student using total marks. Assume
the total of all the courses marks is 500 or take the total marks from the user as input. 
"""

# Initialize variables
total_marks = 0

# Input the marks for each course
course1 = int(input("course 1: "))
course2 = int(input("course 2: "))
course3 = int(input("course 3: "))
course4 = int(input("course 4: "))
course5 = int(input("course 5: "))

# Calculate the total marks
total_marks = course1 + course2 + course3 + course4 + course5

# Calculate the average marks
average_marks = total_marks / 5  # Assuming 5 courses

# Calculate the percentage
total_possible_marks = 500  # Assuming a total of 500 marks
percentage = (total_marks / total_possible_marks) * 100

# Display the results
print(f"Total marks: {total_marks}")
print(f"Average marks: {average_marks:.2f}")
print(f"Percentage: {percentage:.2f}%")