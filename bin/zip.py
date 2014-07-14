#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import sys
import os


def translate(cond):
    if cond == "全": return "true"
    if cond == "雙全": return "!odd"
    if cond == "單全": return "odd"
    if "巷全" in cond: return "lane===%s" % int(cond[:cond.find("巷全")])
    if "巷雙全" in cond:
        lane = int(cond[:cond.find("巷雙全")])
        return "lane===%s && !odd" % lane
    if "巷單全" in cond:
        lane = int(cond[:cond.find("巷單全")])
        return "lane===%s && odd" % lane
    if "弄全" in cond:
        lane = int(cond[:cond.find("巷單全")])
        return "lane===%s && odd" % lane
    if "至" in cond:
        segs = cond.split("至")
        lower, upper = segs[0], segs[-1]
        if "弄" in cond:
            if cond == "連256弄至399之13號": return "alley===256 && number<=399 && dash<=13"
            if cond == "170巷連1弄至12號": return "lane===170 && alley<=1 && number<=12"
            if cond == "81巷雙222號至270弄": return "lane===81 && !odd && number>=222 && alley<=270"
            # lane = int(cond[:cond.find("巷")])
            # lower = lower[lower.find("巷")+1:]

    return "false"


replacements = [
    ("１段", "一段"),
    ("２段", "二段"),
    ("３段", "三段"),
    ("４段", "四段"),
    ("５段", "五段"),
    ("６段", "六段"),
    ("７段", "七段"),
    ("８段", "八段"),
    ("９段", "九段"),
    ("　", " "),
    ("        ", " "),
    ("       ", " "),
    ("      ", " "),
    ("     ", " "),
    ("    ", " "),
    ("   ", " "),
    ("  ", " ")
]


ofile = open("zip/first.txt", "w")
ifile = open("zipcode.txt", "r")

for line in ifile:
    for repl in replacements:
        line = line.replace(repl[0], repl[1])

    ofile.write(line)

ifile.close()
ofile.close()


ofile = open("zip/second.txt", "w")
ifile = open("zip/first.txt", "r")

for line in ifile:
    fields = line.split(" ")
    fields[4] = "".join(fields[4:])
    ofile.write(",".join(fields[:5]))


ifile.close()
ofile.close()


rules = {"tmp": []}
ifile = open("zip/second.txt", "r")

for line in ifile:
    score = 0
    items = line.split(",")
    (code, cty, dst, srt) = (items[0], items[1], items[2], items[3])
    rule = items[4].rstrip("\n")

    rules[cty] = rules[cty] if cty in rules else {}
    rules[cty][dst] = rules[cty][dst] if dst in rules[cty] else {}

    if not srt in rules[cty][dst]:
        rules[cty][dst][srt] = {
            "tmp": [],
            "out": [],
            "src": []
        }

    rules[cty][dst][srt]["src"].append("%s:%s" % (code, rule))

    if "全" in rule: score += 10000
    if "巷" in rule: score += 1000
    if "弄" in rule: score += 1000
    if "號" in rule: score += 1000
    if "至" in rule: score -= 100
    if "上" in rule: score -= 500
    if "下" in rule: score -= 500
    if "連" in rule: score -= 10
    if "雙" in rule: score -= 50
    if "單" in rule: score -= 50
    if "之" in rule: score += 5
    if "樓" in rule: score += 5

    r = (code, rule, score)
    rules[cty][dst][srt]["tmp"].append(r)


ifile.close()


for c in rules:
    for d in rules[c]:
        for s in rules[c][d]:
            orders = rules[c][d][s].pop("tmp")
            orders = sorted(orders, key=lambda tup: tup[2])
            orders = list(reversed(orders))
            for order in orders:
                result = "%s:%s" % (order[0], order[1])
                rules[c][d][s]["out"].append(result)


ofile = open("zip/answer.json", "w")
json.dump(rules, ofile, indent=4, ensure_ascii=False)
ofile.close()


jshead = "function (lane,alley,number,dash,floor) {'use strict';"
jshead += "var token=(lane)?lane:alley;"
jshead += "token=(token)?token:number;"

jsbody = "if (%s) return '%s';"

jstail = "return '00000';}"


for c in rules:
    for d in rules[c]:
        for s in rules[c][d]:
            original = rules[c][d][s].pop("src")
            js = jshead
            for rule in rules[c][d][s].pop("out"):
                segs = rule.split(":")
                condition = translate(segs[-1])
                zipcode = segs[0]
                js += jsbody % (condition, zipcode)
            js += jstail
            rules[c][d][s] = js


ofile = open("zip/rules.json", "w")
json.dump(rules, ofile, indent=4, ensure_ascii=False)
ofile.close()


sys.exit(0)
