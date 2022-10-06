#!/usr/bin/python3

from_dict = dict()

with open("mbox-short.txt", "rt") as fp:
    for line in fp:
        if line.startswith("From: ") :
            str_arr = line.split()
            if str_arr[1]
