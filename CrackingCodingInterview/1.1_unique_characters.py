#implement an algorithim to find if the strings characters are unique
#try without using data structs

def foo(string):
    for i in string:
        count = 0
        for i2 in string:
            if i == i2:
                count = count + 1
            if count > 1:
                return False
            if count == 0:
                return True

#a sneaky way with less iteration
import unittest

def foo2(string):
    for i in string:
        if string.count(i) > 1:
            return False
        else:
            return True
