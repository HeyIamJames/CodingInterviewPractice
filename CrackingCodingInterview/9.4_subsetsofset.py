"""
return all the subsets of a set  
"""

#psudo code:
#iterate through each subset within the set
#if found make a copy in a new set or reuturn individually


def subset(seq):
    main_set = list(seq)
    if len(main_set) < 1:
        yield main_set
        return

    element = [main_set.pop()]
    for sub_set in subsets(main_set):
        yield sub_set
        yield sub_set + element
