# Write a program to create a function that takes two arguments, name and age, and print their values.
def demo(name, age):
    print(name)
    print(age)

demo("Ben", 25)

# Re-write the same funciton to accept a variable length of arguments (instead of being explicit) and print their values.
def func1(*args):
    for i in args:
        print(i)

func1("Ben", 25)