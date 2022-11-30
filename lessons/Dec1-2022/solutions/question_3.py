noun = input('Enter a noun: ')
number = None

while True:
    try:
        number = int(input('Enter an integer: '))
    except ValueError:
        print("That's not an integer")
    else:
        break

place = input('Enter a place: ')
adjective = input('Enter an adjective: ')

print("Back in my day, if I wanted to buy a {}, I had to work for {} hours down at the old {}. Wow, the sky sure is {} today!".format(
    noun, number, place, adjective))
