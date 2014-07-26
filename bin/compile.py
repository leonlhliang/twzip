#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import json
import sys


def translate(cond):
    if cond == u"全": return "true"
    return "false"


js_head = "function(n){"
js_body = "if(%s)return'%s';"
js_tail = "return'00000';}"


ifile = codecs.open("tmp/weighted.json", "r", encoding="utf-8")
rules = json.loads(ifile.read())
ifile.close()

for c in rules:
    for d in rules[c]:
        for s in rules[c][d]:
            js = js_head
            for rule in rules[c][d][s].pop("weighted"):
                segs = rule.split(":")
                condition = translate(segs[-1])
                zipcode = segs[0]
                js += js_body % (condition, zipcode)
            js += js_tail
            rules[c][d][s] = js

ofile = codecs.open("tmp/result.json", "w", encoding="utf-8")
json.dump(rules, ofile, indent=4, ensure_ascii=False)
ofile.close()


ifile = open("tmp/result.json", "r")
ofile = open("lib.js", "w")

for index, line in enumerate(ifile):
    line = line.replace('": "function', '":function')
    line = line.replace(';}"', ';}')
    line = line.replace('            ', '')
    line = line.replace('        ', '')
    line = line.replace('    ', '')

    if index == 0:
        ofile.write("module.exports = {\n")
    elif line == "}":
        ofile.write("};\n")
    elif "if(true)" in line:
        line = line.replace("if(true)", "")
        line = line.replace("return'00000';", "")
        ofile.write(line)
    else:
        ofile.write(line)

ofile.close()
ifile.close()


sys.exit(0)
