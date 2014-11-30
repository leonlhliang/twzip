#!/usr/bin/env python
# -*- encoding: utf8 -*-
import json
import sys


INDEX = {
    "AREA": 5 + 3 * 3 + 3 * 3,
    "CITY": 5 + 3 * 3,
    "CODE": 5
}

result = {}

for line in open("ORIGIN.txt"):
    line = line.replace("１", "一")
    line = line.replace("２", "二")
    line = line.replace("３", "三")
    line = line.replace("４", "四")
    line = line.replace("５", "五")
    line = line.replace("６", "六")
    line = line.replace("７", "七")
    line = line.replace("８", "八")
    line = line.replace("９", "九")

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

    spec = line.replace(road, "").replace("　", "").replace(" ", "")

    if not road in result[city][area]: result[city][area][road] = []
    result[city][area][road].append("%s:%s" % (code, spec))


json.dump(result, open("zipcode.json", "w"),
    ensure_ascii=False,
    indent=4
)

sys.exit(0)
