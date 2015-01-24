#!/usr/bin/env python
# -*- encoding: utf8 -*-
import json
import sys
import web


SCRIPT, USERNAME, PASSWORD = sys.argv


name = {}

for line in open("doc/name.csv"):
    vals = line.strip().split(",")

    if vals[1] == "釣魚台": continue

    zh_tw_city = unicode(vals[1][:9], "utf-8")
    zh_tw_dist = unicode(vals[1][9:], "utf-8")
    en_us_dist = vals[2].replace('"', '').replace("Dist.", "District")
    en_us_city = vals[3].strip().replace('"', '')

    name[zh_tw_city] = en_us_city
    name[zh_tw_dist] = en_us_dist


infile = open("src/rule.json")
data = json.load(infile)
infile.close()


db = web.database(
    use_unicode=0,
    charset="utf8",
    host="localhost",
    user=USERNAME,
    dbn="mysql",
    db="postal",
    pw=PASSWORD
)

for city in data:
    city_enus = name.get(city, city)
    city_id = db.insert("city",
        name_zhtw=city,
        name_enus=city_enus)
    for district in data[city]:
        district_enus = name.get(district, district)
        district_id = db.insert("district",
            name_zhtw=district,
            name_enus=district_enus,
            id_city=city_id)
        for street in data[city][district]:
            street_id = db.insert("street",
                name_zhtw=street,
                name_enus=street,
                id_district=district_id)

print "done."
