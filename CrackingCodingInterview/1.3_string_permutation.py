"""
check if a string is a permutation of anohter string
"""

#utalize sorted, perhaps check length first to make faster

def Permutation(string1,string2):
      if len(string1)!=len(string2):
          return False
      return sorted(string1) == sorted(string2)
