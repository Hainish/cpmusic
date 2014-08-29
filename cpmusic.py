#!/usr/bin/env python
import sys
import humanfriendly

def usage():
    print "Copy a specifically sized random selection of albums"
    print ""
    print "Usage:"
    print sys.argv[0] + " <size> <source> <destination>"
    print "Assumes the source descendents directory structure is <artist>/<album>/"

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
