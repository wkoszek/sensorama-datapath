#!/usr/bin/env python
# Copyright (c) 2015, Wojciech A. Koszek
# All rights reserved.

import sys
import json

def fields_must_have():
	return ["date", "device", "desc", "interval", "sensors", "points" ]

def js_validate(js):
	for field in fields_must_have():
		if field not in js:
			print "missing field " + field
			return False
	sensors = js["sensors"]
	if len(sensors) <= 0:
		print "no sensors? quite impossible"
		return False
	points = js["points"]
	data1 = points[0]

	lengths = [
		("acc", 3),
		("grav", 3),
		("steps", 1),
		("env", 4),
		("bat", 1),
	]
	for l in lengths:
		name = l[0]
		exp_len = l[1]
		if len(data1[name]) != exp_len:
			print "Wrong number of data items in " + name
			print "Expected " + str(exp_len)
			return False
	return True

def check_file(fn):
    sys.stdout.write("# fn={0} ".format(fn))

    rv = 0
    try:
        with open(fn, "r") as f:
            js = json.load(f)
        f.close()

	json.dumps(js, sort_keys=True, indent=4, separators=(',', ': '))

	i = js_validate(js)
	if i == True:
		print "OK"
	else:
		print "Data format is wrong"
    except Exception as e:
        print "Exception: " + repr(e)
        rv = 1

    return rv

def usage():
    print "validate.py <json1file> [<json2file> ...]"
    sys.exit(1)

def main():
    if len(sys.argv) < 2:
        usage()

    rv = 0
    for fn in sys.argv[1:]:
        rv += check_file(fn)

    return rv

if __name__ == "__main__":
    sys.exit(main())

