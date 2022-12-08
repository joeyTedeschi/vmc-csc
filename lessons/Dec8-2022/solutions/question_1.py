# Write a program to create a function that takes two arguments, name and age, and print their values.
# If no values are entered, it should default to your name and age
def demo(name='Stefano', age=1000):
    print(name)
    print(age)


# Re-write the same function to accept a variable length of arguments (instead of being explicit) and print their values.
def func1(*args):
    for i in args:
        print(i)


demo("Ben", 25)
func1("Ben", 25)
