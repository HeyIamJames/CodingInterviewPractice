#add two numbers without using operators
"""
18.1 Write a function that adds two numbers. You should not use + or any arithmetic
operators.
"""


def foo(a, b):
"""iterate through a and b, count iteration via a list, check len"""
    x = []
    for i in range(a):
            x.append(a)
    for i in range(b):
            x.append(b)
    print len(x)
