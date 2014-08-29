#!/usr/bin/env python
import sys
import humanfriendly

def usage():
    print sys.argv[0] + " <size> <source> <destination>"

if __name__ == "__main__":
    if len(sys.argv) != 4:
        usage()
        exit()
    else:
        try:
            size = humanfriendly.parse_size(sys.argv[1])
        except humanfriendly.InvalidSize:
            usage()
            exit()
