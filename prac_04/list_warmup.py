numbers = [3, 1, 4, 1, 5, 9, 2]
# numbers[0] = 3
# numbers[-1] = 2
# numbers[3] = 1
# numbers[:-1] = [3, 1, 4, 1, 5, 9] # index 0 (default) to -1 non-inclusive
# numbers[3:4] = [1]
# 5 in numbers = True
# 7 in numbers = False
# "3" in numbers = False
# numbers + [6, 5, 3] = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

print(numbers[0])
print(numbers[-1])
print(numbers[3])
print(numbers[:-1])
print(numbers[3:4])
print(5 in numbers)
print(7 in numbers)
print("3" in numbers)
print(numbers + [6, 5, 3])
print("--------")

# # Question 1
numbers[0] = "ten"
print(numbers)
# # Question 2
numbers[-1] = 1
print(numbers)
# # Question 3
print(numbers[2:])
# # Question 4
print(9 in numbers)

