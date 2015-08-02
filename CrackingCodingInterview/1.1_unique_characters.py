#implement an algorithim to find if the strings characters are unique


def foo2(string):
    for i in string:
        count = 0
        for i2 in string:
            if i == i2:
                count = count + 1
            if count > 1:
                return False
            if count == 0:
                return True
