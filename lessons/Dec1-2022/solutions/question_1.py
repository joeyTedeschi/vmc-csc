num1 = 10
num2 = int(input('Enter a number greater than 10: '))

while num2 <= num1:
    num2 = int(input('Please enter a number larger than 10: '))

for number in range(num1, num2 + 1):
    if number % 2 == 0:
        print(number)
