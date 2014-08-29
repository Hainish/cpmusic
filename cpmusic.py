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

class AlbumBuilder:
    def __init__(self, source):
        self.source = source

    def get_size(start_path = '.'):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(start_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
        return total_size

    def build_selection(self):
        albums = []
        for artist_name in os.listdir(self.source):
            artist_path = os.path.join(self.source, artist_name)
            if os.path.isdir(artist_path):
                for album_name in os.listdir(artist_path):
                    album_path = os.path.join(artist_path, album_name)
                    if os.path.isdir(album_path):
                        albums.append(album_path)
        self.selection = albums


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
        builder = AlbumBuilder(sys.argv[2])
        builder.build_selection()
