#!/usr/bin/env python
import sys
import os
import humanfriendly
import random
import shutil

def usage():
    print "Copy a specifically sized random selection of albums"
    print ""
    print "Usage:"
    print sys.argv[0] + " <size> <source> <destination>"
    print "Assumes the source descendents directory structure is <artist>/<album>/"

class AlbumBuilder:
    def __init__(self, source):
        self.source = source

    @staticmethod
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

    def choose_albums(self, max_size):
        selection = self.selection
        current_size = 0
        albums = []
        while True:
            album = random.choice(selection)
            album_size = self.get_size(album)
            if current_size + album_size > max_size:
                break
            else:
                albums.append(album)
                selection.remove(album)
                current_size += album_size
        return albums


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
        album_paths = builder.choose_albums(size)
        for album_path in album_paths:
            album_name = os.path.basename(album_path)
            artist_name = os.path.basename(os.path.dirname(album_path))
            shutil.copytree(album_path, os.path.join(sys.argv[3], artist_name, album_name))
