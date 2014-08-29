#!/usr/bin/env python
import sys
import os
import humanfriendly

def usage():
    print "Copy a specifically sized random selection of albums"
    print ""
    print "Usage:"
    print sys.argv[0] + " <size> <source> <destination>"
    print "Assumes the source descendents directory structure is <artist>/<album>/"

def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

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
