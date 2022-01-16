#e. Write a Python program to find the most common elements and their counts from list, tuple, dictionary.
def most_CommonList(List):
    counter = 0
    num = List[0]

    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency > counter):
            counter = curr_frequency
            num = i

    return num, counter


List = [1, 2, 3, 4, 2, 5, 1]
ans = most_CommonList(List)
print(f'Your most common Elements in list is {ans[0]} and this is repeat {ans[1]} times.')

# element in a tuple


def commonElement_tuple(List):
    counter = 0
    num = List[0]

    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency > counter):
            counter = curr_frequency
            num = i

    return num, counter


List = (2, 4, 6, 2, 5, 3, 1, 2, 3)
ans1 = commonElement_tuple(List)
print(f'Your most common Elements in tuple is {ans1[0]} and this is repeat {ans1[1]} times.')


# most common elements in dictionary
a = {'a': 0, 'b': 1, 'c': 2, 'd': 0, 'e': 1,'f':2}
list = []
for i in a.values():
    list.append(i)


def most_CommonDictionary(List):
    counter = 0
    num = List[0]

    for j in List:
        curr_frequency = List.count(j)
        if(curr_frequency > counter):
            counter = curr_frequency
            num = j

    return num, counter


ans2 = most_CommonDictionary(list)
print(f'Your most common Elements in Dicionary is {ans2[0]} and this is repeat {ans2[1]} times.')
