#a. Write a Python script to check whether a given key already exists in a dictionary.
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


def is_key_present(d1):
    if d1 in d:
        print('Key is exists')
    else:
        print('Key does not exists')


is_key_present(10)
is_key_present(1)
