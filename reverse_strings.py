"""
make a function which:
reverse a string such that "dog cat world"
becomes "world cat dog"
"""

"""
psudo code
store each word, break on white space
return in reverse
- possible to do in place by switching all word positions,
then reverse recursively
"""

    def reversestring(str):
      " ".join(str.split()[::-1])
