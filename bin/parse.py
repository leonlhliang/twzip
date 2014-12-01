#!/usr/bin/env python
# -*- encoding: utf8 -*-
import json
import sys


INDEX = {
    "AREA": 5 + 3 * 3 + 3 * 3,
    "CITY": 5 + 3 * 3,
    "CODE": 5
}

raw = {}

for line in open("ORIGIN.txt"):
    line = line.replace("１", "一").replace("２", "二").replace("３", "三")
    line = line.replace("４", "四").replace("５", "五").replace("６", "六")
    line = line.replace("７", "七").replace("８", "八").replace("９", "九")

    code = line[:INDEX["CODE"]]
    city = line[INDEX["CODE"]: INDEX["CITY"]]

    area_index = 0 if line[INDEX["AREA"]] == " " else 3
    area_index += INDEX["AREA"]
    area = line[INDEX["CITY"]: area_index].strip()

    line = line[area_index:].strip()
    road = line[:-3] if len(line.split(" ")) == 1 else line.split(" ")[0]
    spec = line.replace(road, "").replace("　", "").replace(" ", "")

    weight = 0

    if "全" in spec: weight += (pow(10, 6) + pow(2, 0))
    if "巷" in spec: weight += (pow(10, 5) + pow(2, 4))
    if "弄" in spec: weight += (pow(10, 5) + pow(2, 3))
    if "號" in spec: weight += (pow(10, 5) + pow(2, 2))
    if "之" in spec: weight += (pow(10, 5) + pow(2, 1))
    if "樓" in spec: weight += (pow(10, 5) + pow(2, 0))
    if "上" in spec: weight -= (pow(10, 4) - pow(2, 1))
    if "下" in spec: weight -= (pow(10, 4) - pow(2, 0))
    if "至" in spec: weight -= (pow(10, 3) - pow(2, 0))
    if "雙" in spec: weight -= (pow(10, 2) - pow(2, 5))
    if "單" in spec: weight -= (pow(10, 2) - pow(2, 0))
    if "連" in spec: weight -= (pow(10, 1) - pow(2, 0))

    key = (city, area, road)
    if not key in raw: raw[key] = []
    raw[key].append((code, spec, weight))


result = {}

for reg in raw:
    specs = list(reversed(sorted(raw[reg], key=lambda tup: tup[2])))
    city, area, road = reg[0], reg[1], reg[2]
    if not city in result: result[city] = {}
    if not area in result[city]: result[city][area] = {}
    result[city][area][road] = []
    for spec in specs:
        result[city][area][road].append("%s:%s" % (spec[0], spec[1]))


json.dump(result, open("zipcode.json", "w"),
    ensure_ascii=False,
    indent=4
)

sys.exit(0)
