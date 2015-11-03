#!/usr/bin/env python
# Copyright (c) 2015, Wojciech A. Koszek
# All rights reserved.

import sys
import json

def check_file(fn):
    sys.stdout.write("# fn={0} ".format(fn))

    rv = 0
    try:
        with open(fn, "r") as f:
            js = json.load(f)
        f.close()

        js = json.dumps(js, sort_keys=True, indent=4, separators=(',', ': '))
        # print js
        print "OK"
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

