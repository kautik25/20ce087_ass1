#e. Write a Python script to concatenate following dictionaries to create a new one.
d1={1:100, 2:110}
d2={3:120, 4:130}
d3={5:140,6:150}

d4 = {}
for i in (d1, d2, d3):
    print('i', i)
    d4.update(i)
print(d4)