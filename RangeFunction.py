"""Use the range function to print the numbers from 40 to 1 (backwards)"""
x = 40
for i in range(39):
    x = x - 1
    print(x)
for i in range(40, 1, -1):
    print (i)

"""Repeat the exercise but count by 5's"""

def by5():
    y = 40
    while y > 0:
        if y % 5 == 0:
            print (y)
        y = y - 1
by5()
for i in range(40, 1, -5):
    print (i)

"""Write a program that will count print all the multiples of (n) where n is
taken from user input.  Include necessary print statements."""
print("Enter a number.")
m = int(input())
def multiples(m, count):
    for i in range(0,count*m,m):
        print(i)
multiples(m, 10)
