"""Use the range function to print the numbers from 40 to 1 (backwards)"""
x = 40
for i in range(39):
    x = x - 1
    print(x)


"""Repeat the exercise but count by 5's"""

def by5():
    y = 40
    while y > 0:
        if y % 5 == 0:
            print (y)
        y = y - 1
by5()


"""Write a program that will count print all the multiples of (n) where n is
taken from user input.  Include necessary print statements."""
