#!/usr/bin/python3

import json
total = 0
with open('movie.json', "rt") as fp:
    json_data = json.load(fp)
    movie_list = json_data["movie"]
    for item in movie_list:
        salesAmt = int(item["salesAmt"])
        total += salesAmt
print("오늘 매출액은 총 " + str(total) + "원")
