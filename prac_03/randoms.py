# import random

# print(random.randint(5, 20))  # line 1
# print(random.randrange(3, 10, 2))  # line 2
# print(random.uniform(2.5, 5.5))  # line 3

# Q1: What did you see on line 1?
# 18, 7, 16, 15, 10, 10, 14, 10
# Random numbers in between 5 (smallest) and 20 (largest) inclusive

# Q2: What did you see on line 2?
# 9, 9, 7, 5, 3, 5, 7, 7, 7, 5, 9
# Random numbers between 3 and 10.
# Except it cant print 2 because it starts at 3 and goes up in 2's (odd numbers only).

# Q3: What did you see on line 3?
# 4.517992705631505, 4.7708081429297025, 3.216956853839124, 3.701802003696305, 4.1872939785570455 , 2.5931191252522168
# Specific random between 2.5 (smallest) and 5.5 (largest) resulting in many decimal places
# The odds of getting 2.5 or 5.5 exactly however are very unlikely

# Q4:
import random

print(random.randint(1, 100))
