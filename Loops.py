"""Write a program that will add 5 and loop until it reaches a number GREATER
than 100.  It should then spit out the result AND tell the user how many times
it had to add 5 (if any)"""
def add5(io):
    oi = 0
    while io < 100:
        io = io + 5
        oi = oi + 1
    print(io)
    print(oi)
add5(5)
"""Write a program that will prompt the user for an input value (n) and double
it IF is an ODD number, triple it if is an EVEN number and do nothing if it is
anything else (like a decimal or a string)"""
