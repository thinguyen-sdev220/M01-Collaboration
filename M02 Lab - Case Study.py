# Author: Thi Nguyen
# File Name: M02 Lab - Case Study.py
# (Description: This Python app accepts student names and GPAs and tests if the student qualifies 
# for either the Dean's List or the Honor Roll)

# Ask student's last name
last_name = input("Enter student's last name or ZZZ to quit: ")

# Loop to ask student's first name and GPA if student's last name is not ZZZ, then 
while last_name != 'ZZZ':
    first_name = input("Enter student's first name: ")
    gpa = float(input("Enter student's GPA: "))
    # Check if student is in Dean List or Honor Roll
    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List.")
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll.")
    else:
        print(f"{first_name} {last_name} does not qualify for Dean's List or Honor Roll.")
    # Ask student's last name
    last_name = input("Enter student's last name or ZZZ to quit: ")
    
