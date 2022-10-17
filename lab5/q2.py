#!/usr/bin/python3
a = []
b = []
for i in range(1, 11):
    a.append(i)
    b.append(i**2)
dictionary = dict(zip(a, b))
print(dictionary[6])
