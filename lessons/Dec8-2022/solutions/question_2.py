# Write a program to create a function called show_employee()

# It should accept the employee’s name and salary as arguments.
# If the salary is missing in the function call then assign a default value of 9000 to salary
# Display both values

def show_employee(name, salary=9000):
    print("Name:", name, "salary:", salary)

show_employee("Ben", 12000)
show_employee("Jessa")