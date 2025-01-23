"""Delete the recording with uuid from the short metadata file."""

import argparse
import os
import pickle
import shelve
import sys
from pathlib import Path
from pprint import pprint

from genrespec import genre_spec
from common.constants import METADATA, SHORT
from common.types import RecordingTuple, TrackTuple
from common.utilities import config


parser = argparse.ArgumentParser(
        prog=Path(sys.argv[0]).stem,
        description='Print contents of data file short.')

parser.add_argument('-g', '--genre', default='all',
        help='genre (default: all)')
parser.add_argument('-u', '--uuid',
        help='uuid')

args = parser.parse_args()

for genre in genre_spec:
    if args.genre != 'all' and genre != args.genre:
        continue

    short_file_path = Path(SHORT, genre)
    tmp_file_path = Path(str(short_file_path) + '.tmp')
    with open(short_file_path, 'rb') as short_fo, \
            open(tmp_file_path, 'wb') as tmp_fo:
        while True:
            try:
                line = pickle.load(short_fo)
            except EOFError:
                print('EOFError')
                break

            *short_metadata, uuid, work_index = line
            if uuid != args.uuid:
                pickle.dump(line, tmp_fo)
            else:
                print(f'skipping uuid {uuid} in genre {genre}')

    tmp_file_path.rename(short_file_path)

