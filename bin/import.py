#!/usr/bin/env python
import json
import sys
import web

SCRIPT, USERNAME, PASSWORD = sys.argv

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
    id_city = db.select("city",
        where="name_zhtw=$city",
        vars=locals())
    if not id_city:
        id_city = db.insert("city",
            name_zhtw=city,
            name_enus=city,
            alias=city)
    else:
        id_city = id_city[0].id
    for district in data[city]:
        id_district = db.select("district",
            where="name_zhtw=$district",
            vars=locals())
        if not id_district:
            id_district = db.insert("district",
                name_zhtw=district,
                name_enus=district,
                alias=district)
        else:
            id_district = id_district[0].id
        for street in data[city][district]:
            id_street = db.select("street",
                where="name_zhtw=$street",
                vars=locals())
            if not id_street:
                id_street = db.insert("street",
                    name_zhtw=street,
                    name_enus=street,
                    alias=street)
            else:
                id_street = id_street[0].id
            id_region = db.insert("region",
                id_district=id_district,
                id_street=id_street,
                id_city=id_city)

print "done."
