#example
for i in range(1, 21, 2):
    print(i, end=' ')
print()

#0 to 100 in 10's
for i in range(0, 101, 10):
    print(i, end=' ')
print()

#20 to 1 counting down
for i in range(20, 0, -1):
    print(i, end=' ')
print()

#n number of stars
number_of_stars = int(input("Number of stars: "))
for i in range(0, number_of_stars):
    print("*", end='')
print()

#n lines of increasing stars
number_of_stars = int(input("Number of stars: "))
for i in range(1, number_of_stars + 1):
    print('*' * i)
print()
