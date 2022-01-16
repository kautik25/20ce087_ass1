#c. Write a Python program to sum all the items in a dictionary.
def returnSum(l1):

    list = []
    for i in l1:
        list.append(l1[i])
    ans = sum(list)

    return ans


# Driver Function
dict = {'a': 10, 'b': 15, 'c': 20, 'd': 25}
print(" Sum of all items in a Dictionary:", returnSum(dict))
