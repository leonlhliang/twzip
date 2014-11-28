#!/usr/bin/env python
# -*- encoding: utf8 -*-
import json


result = {}

index = {
    "area": 5 + 3 * 3 + 3 * 3,
    "city": 5 + 3 * 3,
    "code": 5
}

for line in open("ORIGIN.txt"):
    code = line[:index["code"]]

    city = line[index["code"]: index["city"]]
    if not city in result: result[city] = {}

    area = line[index["city"]: index["area"]]
    if not area in result[city]: result[city][area] = {}

    line = line[line.find(" "):].strip()

    road = line[:line.find(" ")]
    condition = line[line.find(" "):].replace("　", "").strip()


json.dump(result, open("zipcode.json", "w"),
    ensure_ascii=False,
    indent=4
)
