#!/usr/bin/env python
import sys

def usage():
    print sys.argv[0] + " <size> <source> <destination>"

if __name__ == "__main__":
    if len(sys.argv) != 4:
        usage()
