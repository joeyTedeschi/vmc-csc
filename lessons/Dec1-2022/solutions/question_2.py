original = input(
    "Enter a word or sentence and I'll tell you if it's a palindrome: ")

reversed_original = ""

for letter in original:
    reversed_original = letter + reversed_original

if reversed_original == original:
    print('This is a palindrome!')
else:
    print('This is not a palindrome')
