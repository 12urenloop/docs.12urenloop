#!/usr/bin/env python

import sys
from os.path import exists

USAGE = """Usage: lenny.py {input_file} {output_file_name}

Remove leading checkmarks from the input file"""

CHECKMARK_PREFIX = "X "

if len(sys.argv) != 3:
	print("Wrong number of arguments")
	print(USAGE)
	sys.exit(1)

if not exists(sys.argv[1]):
	print(f"'{sys.argv[1]}' is not a file")
	print(USAGE)
	sys.exit(1)

with open(sys.argv[1], "r") as infile:
	data = infile.readlines()

for i, line in enumerate(data):
	if line.lstrip().startswith(CHECKMARK_PREFIX):
		x_index = line.find(CHECKMARK_PREFIX) + len(CHECKMARK_PREFIX)
		data[i] = line[x_index:]

with open(sys.argv[2], "w+") as outfile:
	outfile.writelines(data)
