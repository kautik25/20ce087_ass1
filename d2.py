#b. Write a Python script to merge two Python dictionaries.
def Merge(dict1, dict2):

    return(dict1.update(dict2))
     
# Driver code
dict1 = {'a1': "red", 'a2': "blue"}
dict2 = {'a3': "yellow", 'a4': "green"}
 
# This return None
Merge(dict1, dict2)
 
# changes made in dict2
print(dict1)