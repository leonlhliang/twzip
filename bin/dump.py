#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import sys
import os


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


ifile = open("tmp/original.txt", "r")
ofile = open("tmp/replaced.txt", "w")

for line in ifile:
    for repl in replacements:
        line = line.replace(repl[0], repl[1])

    ofile.write(line)

ifile.close()
ofile.close()


ifile = open("tmp/replaced.txt", "r")
ofile = open("tmp/formatted.txt", "w")

for line in ifile:
    fields = line.split(" ")
    fields[4] = "".join(fields[4:])
    ofile.write(",".join(fields[:5]))

ifile.close()
ofile.close()

os.remove("tmp/replaced.txt")


ifile = open("tmp/formatted.txt", "r")
rules = {"tmp": []}

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
            "weighted": [],
            "original": []
        }

    rules[cty][dst][srt]["original"].append("%s:%s" % (code, rule))

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
                rules[c][d][s]["weighted"].append(result)


ofile = open("tmp/reference.json", "w")
json.dump(rules, ofile, indent=4, ensure_ascii=False)
ofile.close()


for c in rules:
    for d in rules[c]:
        for s in rules[c][d]:
            original = rules[c][d][s].pop("original")


ofile = open("tmp/weighted.json", "w")
json.dump(rules, ofile, indent=4, ensure_ascii=False)
ofile.close()


sys.exit(0)


