#b. Write a Python program to remove an item from a set if it is present in the set.
def isRemove(element):
    if element in s:
        s.discard(element)
        return s
    else:
        return 'This element does not exist in set'


s = set([10, 20, 30, 40])
print(isRemove(30))
