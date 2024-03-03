import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1?
# The output is a random integer between 5 and 20, including both 5 and 20.

# What was the smallest number you could have seen, what was the largest?
# Largest: 20
# Smallest: 5

# What did you see on line 2?
# The output is a random integer from the range 3 to 9, with the gap of 2 numbers.

# What was the smallest number you could have seen, what was the largest?
# Smallest: 3
# Largest: 9

# Could line 2 have produced a 4?
# No, because the step is 2 starting from 3, so it produces only odd numbers.

# What did you see on line 3?
# The output is a random float number between 2.5 and 5.5.

# What was the smallest number you could have seen, what was the largest?
# Smallest: 2.5
# Largest: 5.5

random_number = random.randint(1, 100)
print(random_number)