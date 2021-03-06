"""
Given a source word, target word and an English dictionary, 
transform the source word to target by changing/adding/removing 1 character at a time, 
while all intermediate words being valid English words. Return the transformation chain
which has the smallest number of intermediate words.
http://www.ardendertat.com/2011/10/17/programming-interview-questions-8-transform-word
"""

def constructGraph(dictionary):
    graph=collections.defaultdict(list) 
    letters=string.lowercase 
    for word in dictionary:
        for i in range(len(word)):
         #remove 1 character
         remove=word[:i]+word[i+1:] 
         if remove in dictionary:
             graph[word].append(remove)
