#!/usr/bin/env python
# -*- encoding: utf8 -*-
import json
import sys


result = {}

INDEX = {
    "AREA": 5 + 3 * 3 + 3 * 3,
    "CITY": 5 + 3 * 3,
    "CODE": 5
}

for line in open("ORIGIN.txt"):
    code = line[:INDEX["CODE"]]

    city = line[INDEX["CODE"]: INDEX["CITY"]]
    if not city in result: result[city] = {}

    area_index = INDEX["AREA"]
    if line[INDEX["AREA"]] != " ": area_index += 3
    area = line[INDEX["CITY"]: area_index].strip()
    if not area in result[city]: result[city][area] = {}

    line = line[area_index:].strip()

    road = line.split(" ")[0]
    if len(line.split(" ")) == 1: road = line[:-3]
    if not road in result[city][area]: result[city][area][road] = {}

    condition = line[line.find(" "):].replace("　", "").strip()


json.dump(result, open("zipcode.json", "w"),
    ensure_ascii=False,
    indent=4
)

sys.exit(0)
