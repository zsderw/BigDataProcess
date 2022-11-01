#!/usr/bin/python3
import sys
from datetime import datetime, date

dictt=dict()
readfile = sys.argv[1]
writefile = sys.argv[2]

def funcday(date):
    weeks = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    day = date.weekday()
    return weeks[day]

with open(readfile, "rt") as fp:
    for line in fp:
        arr = list(map(lambda x : x.strip(), line.split(',')))
        arr2 = list(map(lambda x : int(x), arr[1].split('/')))
        day2 = arr[0] + "," + funcday(date(arr2[2], arr2[0], arr2[1]))

        if day2 not in dictt:
            dictt[day2] = [int(arr[2]), int(arr[3])]
        else:
            dictt[day2][0] += int(arr[2])
            dictt[day2][1] += int(arr[3])

with open(writefile, "wt") as fp2:
    for key, value in dictt.items():
        s = key + " " + str(value[0]) + "," + str(value[1]) + "\n"
        fp2.write(s)

