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

    area = line[INDEX["CITY"]: INDEX["AREA"]]
    if not area in result[city]: result[city][area] = {}

    line = line[line.find(" "):].strip()

    road = line[:line.find(" ")]
    condition = line[line.find(" "):].replace("　", "").strip()


json.dump(result, open("zipcode.json", "w"),
    ensure_ascii=False,
    indent=4
)

sys.exit(0)
