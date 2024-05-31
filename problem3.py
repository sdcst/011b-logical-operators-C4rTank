#! python3
"""
Problem 3
Pythagorean triples are sets of 3 integers such that the squares of the 2 smaller numbers is equal to the square of the third.
Ask the user to enter in 3 numbers, in any order.  Order the numbers from smallest to largest.
Determine if they form a Pythagorean triple. 

You can use max() to help you find the largest number
You can use min() to help you find the smallest number
How can we find the middle number though?
(2 marks)

Inputs:
an integer
an integer
an integer

Outpus:
xx,yy,zz form a Pythagorean Triple
xx,yy,zz do not form a Pythagorean Triple

Examples:
Enter an integer=>3
Enter an integer=>5
Enter an integer=>4
3,4,5 form a Pythagorean triple

Enter an integer=>5
Enter an integer=>4
Enter an integer=>2
2,4,5 do not form a Pythagorean triple
"""

import math

a = int(input("Input a number: " ))
b = int(input("Input a number: " ))
c = int(input("Input a number: " ))

nums = [a, b, c]
nums = nums.sort()

a2 = math.pow(a,2)
b2 = math.pow(b,2)
c2 = math.pow(c,2)

hyp = max(a2,b2,c2)

if hyp == a2:
    if b2 + c2 == a2:
        print(a,b,c,"form a Pythagorean Triple")
    else:   
        print(a,b,c,"do NOT form a Pythagorean Triple")

if hyp == b2:
    if a2 + c2 == b2:
        print(a,b,c,"form a Pythagorean Triple")
    else:   
        print(a,b,c,"do NOT form a Pythagorean Triple")

if hyp == c2:
    if a2 + b2 == c2:
        print(a,b,c,"form a Pythagorean Triple")
    else:   
        print(a,b,c,"do NOT form a Pythagorean Triple")

#done









