#a. Write a Python program to add member(s) in a set and clear a set
s = set([1,2])  
print('first', s)
s.update([3,4])
print('second', s)
s.clear()
print(s)