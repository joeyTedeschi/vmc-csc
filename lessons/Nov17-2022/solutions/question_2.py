# Let's practice using some of the operators we've seen

# 📝 Create 2 different number variables in 1 line

# 📝 Now let's do some checks with these numbers!
# If their product is greater than 100, let's print their product
# If their product is a negative number, let's print out "Only positive numbers please!"
# If neither condition is fulfilled, let's print the sum of both numbers
# 🙋In all situations, our print statement should make it clear what result we're seeing

num1, num2 = 10, -2

if num1 * num2 > 100:
    print('This is the product: ' + str(num1 * num2))
elif num1 * num2 < 0:
    print('Only positive numbers please!')
else:
    print('This is the sum: ' + str(num1 + num2))
