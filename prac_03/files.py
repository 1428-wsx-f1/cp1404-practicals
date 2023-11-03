# Question 1

name = input("Enter Name: ")
name_file = open("name.txt", "w")
print(name, file=name_file)
name_file.close()

# Question 2
read_name_file = open("name.txt", "r")
name = read_name_file.read()
print(f"Your name is {name}")
name_file.close()

# Question 3
with open("numbers.txt", "r") as read_numbers_file:
    result = int(read_numbers_file.readline()) + int(read_numbers_file.readline())
    print(f"Result is {result}")

# Question 4
with open("numbers.txt", "r") as read_numbers_file:
    total = 0
    for line in read_numbers_file:
        number = int(line)
        total += number
    print(f"Total is {total}")
