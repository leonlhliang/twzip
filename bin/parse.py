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
    line = line.replace("１", "一").replace("２", "二").replace("３", "三")
    line = line.replace("４", "四").replace("５", "五").replace("６", "六")
    line = line.replace("７", "七").replace("８", "八").replace("９", "九")

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

    weight = 0

    if "全" in spec: weight += (pow(10, 6) + 0)
    if "巷" in spec: weight += (pow(10, 5) + 4)
    if "弄" in spec: weight += (pow(10, 5) + 3)
    if "號" in spec: weight += (pow(10, 5) + 2)
    if "之" in spec: weight += (pow(10, 5) + 1)
    if "樓" in spec: weight += (pow(10, 5) + 0)
    if "上" in spec: weight -= (pow(10, 4) + 1)
    if "下" in spec: weight -= (pow(10, 4) + 0)
    if "至" in spec: weight -= (pow(10, 3) + 0)
    if "雙" in spec: weight -= (pow(10, 2) + 5)
    if "單" in spec: weight -= (pow(10, 2) + 0)
    if "連" in spec: weight -= (pow(10, 1) + 0)

    if not road in result[city][area]: result[city][area][road] = []
    result[city][area][road].append("%s:%s:%s" % (code, spec, weight))


json.dump(result, open("zipcode.json", "w"),
    ensure_ascii=False,
    indent=4
)

sys.exit(0)
