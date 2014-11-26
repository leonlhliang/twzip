#!/usr/bin/env python
# -*- encoding: utf8 -*-

zip_digits = 5
city_chars = 3

for line in open("ORIGIN.txt"):
    zipcode = line[:zip_digits]
    city = line[zip_digits: zip_digits + (city_chars*3)]
    district = line[zip_digits + (city_chars*3): line.find(" ")]

    line = line[line.find(" "):].strip()

    street = line[:line.find(" ")]
    condition = line[line.find(" "):].replace("　", "").strip()

    print condition

