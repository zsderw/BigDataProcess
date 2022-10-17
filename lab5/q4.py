#!/usr/bin/python3

fname = input("Enter file name : ")

from_dict = dict()

with open(fname, "rt") as fp:
    for line in fp:
        if line.startswith("From: ") :
            str_arr = line.split()
            if str_arr[1]
