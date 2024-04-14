"""
Question 1
A ValueError will occur if the user enters something that is not a valid integer when prompted for the numerator
 or denominator. For example, entering a string or a float beside from the requirement.

Question 2
A ZeroDivisionError will occur if the user enters 0 as the denominator because dividing any number
 by zero is undefined in mathematics.

Question 3
Yes, it can avoid the possibility of a ZeroDivisionError by checking if the denominator is zero before performing
the division.
"""


try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")
