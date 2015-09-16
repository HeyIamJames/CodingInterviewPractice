"""
given a string, return a string counting all the occurences 
of each character if the count > 1
"""

def compress(string_to_compress):

    if len(string_to_compress) < 2
        return string_to_compress

    groups = []
    previous_character = string_to_compress[0]
    counter = 1

    for c in string_to_compress[1:]:
        if c == previous_character:
            counter += 1
        else:
            groups.append(previous_character + str(counter))
            previous_character = c
            counter = 1
    groups.append(c + str(counter))
    result = ''.join(groups)
    if len(result) < len(string_to_compress):
        return result
    else:
        return string_to_compress
