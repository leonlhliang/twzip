#!/usr/bin/env python
# -*- encoding: utf8 -*-
import shutil
import json
import sys
import os


SCRIPT, SRCDIR, OUTDIR = sys.argv

if not os.path.exists(OUTDIR): os.makedirs(OUTDIR)


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

    length["dist"] = 2 * 3
    while line[length["dist"]] != " " and length["dist"] < 4 * 3:
        length["dist"] += 1

    dist = line[:length["dist"]]
    line = line[length["dist"]:].strip()

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

    key = (city, dist, road)
    if not key in raw: raw[key] = []
    raw[key].append((code, spec, weight))


rule = {}

for region in raw:
    conditions = list(reversed(sorted(raw[region], key=lambda tup: tup[2])))
    city, dist, road = region[0], region[1], region[2]
    if not city in rule: rule[city] = {}
    if not dist in rule[city]: rule[city][dist] = {}
    rule[city][dist][road] = []
    for condition in conditions:
        spec = "%s:%s" % (condition[0], condition[1])
        rule[city][dist][road].append(spec)


json.dump(rule, open(os.path.join(OUTDIR, "rule.json"), "w"),
    ensure_ascii=False,
    indent=4
)


name = {}

for line in open(os.path.join(SRCDIR, "name.csv")):
    vals = line.strip().split(",")

    if vals[1] == "釣魚台": continue

    zh_tw_city = vals[1][:9]
    zh_tw_dist = vals[1][9:]
    en_us_dist = vals[2].replace('"', '').replace("Dist.", "District")
    en_us_city = vals[3].strip().replace('"', '')

    id_city = "".join(en_us_city.split(" ")).lower()
    id_dist = "".join(en_us_dist.split(" ")).lower().replace("’", "")

    if id_city == "nanhaiislands": id_city = "kaohsiungcity"

    name_city = (zh_tw_city, en_us_city)
    name_dist = (zh_tw_dist, en_us_dist)

    if not id_city in name:
        name[id_city] = {"name": name_city, "district": {}}
        outdir = os.path.join(OUTDIR, id_city)
        if not os.path.exists(outdir):
            os.makedirs(outdir)

    if not id_dist in name[id_city]["district"]:
        name[id_city]["district"][id_dist] = name_dist


json.dump(name, open(os.path.join(OUTDIR, "name.json"), "w"),
    ensure_ascii=False,
    indent=4
)

for city in name:
    name_city = name[city]["name"][0]
    for dist in name[city]["district"]:
        name_dist = name[city]["district"][dist][0]
        ofilepath = os.path.join(OUTDIR, "%s/%s.json" % (city, dist))
        json.dump(rule[name_city][name_dist], open(ofilepath, "w"),
            ensure_ascii=False,
            indent=4
        )


sys.exit(0)
