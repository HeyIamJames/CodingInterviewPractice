"""
Given an array:

[a_1, a_2, ..., a_N, b_1, b_2, ..., b_N, c_1, c_2, ..., c_N ]  

convert it to:

[a_1, b_1, c_1, a_2, b_2, c_2, ..., a_N, b_N, c_N]  
"""

def convert(l):
return zip(l[0:len(l)/3],l[len(l)/3:2*len(l)/3],l[2*len(l)/3:])
