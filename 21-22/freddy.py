#!/usr/bin/env python

import sys
from os.path import exists

USAGE = """Usage: freddy.py {input_file} {output_file_name}

Group items in the inventory list by category
You should run lenny.py first to remove checkmarks"""

if len(sys.argv) != 3:
	print("Wrong number of arguments")
	print(USAGE)
	sys.exit(1)

if not exists(sys.argv[1]):
	print(f"'{sys.argv[1]}' is not a file")
	print(USAGE)
	sys.exit(1)

category_map = dict()
current_category = ""

with open(sys.argv[1], "r") as infile:
	for line in infile.readlines():
		if line.lstrip().startswith("#") or line.strip() == "":
			continue

		sep_idx = line.find(" - ")
		category = line[:sep_idx].upper()
		item = line[sep_idx + 3:]

		if category.strip() == "":
			item = category + item
			category = current_category
		else:
			current_category = category

		if category in category_map:
			category_map[category].append(item)
		else:
			category_map[category] = [item]

with open(sys.argv[2], "w+") as outfile:
	for cat in sorted(category_map):
		outfile.write(f"# {cat}\n")
		outfile.writelines(category_map[cat])
		outfile.write("\n")
