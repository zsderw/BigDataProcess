#!/usr/bin/python3
import sys

dictt = dict()

readfile = sys.argv[1]
writefile = sys.argv[2]

with open(readfile, "rt") as fp:
	for line in fp:
    	arr = line.split('::')
        arr2 = list(map(lambda x : x.strip(), arr[2].split('|')))
        for i in arr2:
            if i not in dictt:
                dictt[i] = 1
            else:
                dictt[i] += 1

with open(writefile, "wt") as fp2:
    for key, value in dictt.items():
        s = key + " " + str(value) + "\n"
        fp2.write(s)
