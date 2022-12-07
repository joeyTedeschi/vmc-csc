# Write a Python function to check whether a number falls in a given range.
# The number, as well as the range, should be specified by the user.
# Implement error checks to ensure the values entered are numbers.
# If it does, return the value True. Otherwise return False.
# Then print the result

def check_range(num, lower, upper):
    if num in range(int(lower), int(upper)+1):
        return True
    return False

while True:
    try:
        num = int(input("Enter your number:"))
        lower_limit = int(input("Enter the lower limit of your range:"))
        upper_limit = int(input("Enter the upper limit of your range:"))
        break
    except ValueError:
        print("You did not enter a number, restarting...")


result = check_range(num, lower_limit, upper_limit)
if result:
    print(str(num) + " is in the range")
else:
    print("The number is outside the given range")
