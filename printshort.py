"""Print the contents of the short metadata file for genre."""

import argparse
import pickle
import sys
from pathlib import Path

from genrespec import genre_spec
from common.constants import METADATA, SHORT
from common.types import RecordingTuple, TrackTuple
from common.utilities import config


parser = argparse.ArgumentParser(
        prog=Path(sys.argv[0]).stem,
        description='Print contents of data file short.')

parser.add_argument('-g', '--genre', default='all',
        help='genre (default: all)')

args = parser.parse_args()

for genre in genre_spec:
    if args.genre != 'all' and genre != args.genre:
        continue
    print(genre, config.genre_spec[genre]['primary'])
    short_file_path = Path(SHORT, genre)
    with open(short_file_path, 'rb') as short_fo:
        while True:
            try:
                *short_metadata, uuid, work_index = pickle.load(short_fo)
            except EOFError:
                break
            print(short_metadata, uuid, work_index)
    print()

