#!/usr/bin/env python
# -*- encoding: utf8 -*-
import shutil
import json
import sys
import os


SCRIPT, SRCDIR, OUTDIR = sys.argv


if os.path.exists(OUTDIR): shutil.rmtree(OUTDIR)
os.makedirs(OUTDIR)


length = {
    "city": 3 * 3,
    "code": 5
}

raw = {}

for line in open(os.path.join(SRCDIR, "code.txt")):
    line = line.replace("１", "一").replace("２", "二").replace("３", "三")
    line = line.replace("４", "四").replace("５", "五").replace("６", "六")
    line = line.replace("７", "七").replace("８", "八").replace("９", "九")

    code = line[:length["code"]]
    line = line[length["code"]:]
    city = line[:length["city"]]
    line = line[length["city"]:]

    length["area"] = 2 * 3
    while line[length["area"]] != " " and length["area"] < 4 * 3:
        length["area"] += 1

    area = line[:length["area"]]
    line = line[length["area"]:].strip()

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


rule = {}

for region in raw:
    conditions = list(reversed(sorted(raw[region], key=lambda tup: tup[2])))
    city, area, road = region[0], region[1], region[2]
    if not city in rule: rule[city] = {}
    if not area in rule[city]: rule[city][area] = {}
    rule[city][area][road] = []
    for condition in conditions:
        spec = "%s:%s" % (condition[0], condition[1])
        rule[city][area][road].append(spec)


json.dump(rule, open(os.path.join(OUTDIR, "rule.json"), "w"),
    ensure_ascii=False,
    indent=4
)


name = {}

for line in open(os.path.join(SRCDIR, "name.csv")):
    vals = line.strip().split(",")

    if vals[1] == "釣魚台": continue

    zh_tw_city = vals[1][:9]
    zh_tw_area = vals[1][9:]
    en_us_area = vals[2].replace('"', '').replace("Dist.", "District")
    en_us_city = vals[3].strip().replace('"', '')

    id_city = "".join(en_us_city.split(" ")).lower()
    id_area = "".join(en_us_area.split(" ")).lower().replace("’", "")

    if id_city == "nanhaiislands": id_city = "kaohsiungcity"

    name_city = (zh_tw_city, en_us_city)
    name_area = (zh_tw_area, en_us_area)

    if not id_city in name:
        name[id_city] = {"name": name_city, "area": {}}
        os.makedirs(os.path.join(OUTDIR, id_city))

    if not id_area in name[id_city]["area"]:
        name[id_city]["area"][id_area] = name_area


json.dump(name, open(os.path.join(OUTDIR, "name.json"), "w"),
    ensure_ascii=False,
    indent=4
)

for city in name:
    name_city = name[city]["name"][0]
    for area in name[city]["area"]:
        name_area = name[city]["area"][area][0]
        ofilepath = os.path.join(OUTDIR, "%s/%s.json" % (city, area))
        json.dump(rule[name_city][name_area], open(ofilepath, "w"),
            ensure_ascii=False,
            indent=4
        )


sys.exit(0)
