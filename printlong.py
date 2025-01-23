"""Print the long metadata for recording with uuid."""

import argparse
import shelve
import sys
from pathlib import Path

from common.constants import LONG
from common.types import RecordingTuple, WorkTuple

parser = argparse.ArgumentParser(
        prog=Path(sys.argv[0]).stem,
        description='Print contents of data file long.')

parser.add_argument('uuid',
        help='print long values for recording with uuid')
parser.add_argument('-v', '--verbosity', type=int, default=1,
        help='verbosity level (1-3)')

args = parser.parse_args()

with shelve.open(str(LONG), 'r') as recording_shelf:
    try:
        long_metadata = recording_shelf[args.uuid]
    except KeyError:
        print(f'recording not found: {args.uuid}')
        sys.exit(1)

    print(f'-- common {"-"*66}')
    print('tracks =', long_metadata.tracks, end='\n'*2)
    print('props =', long_metadata.props, end='\n'*2)
    print('discids =', long_metadata.discids, end='\n'*2)

    works = dict(sorted(long_metadata.works.items()))
    for i, work in works.items():
        print(f'-- work {i} {"-" * 66}')
        if args.verbosity >= 1:
                print('genre =', work.genre, end='\n'*2)
                print('metadata =', work.metadata, end='\n'*2)
                print('props =', work.props, end='\n'*2)
                print('tracks_ids =', work.track_ids, end='\n'*2)
        if args.verbosity >= 2:
                print('nonce =', work.nonce, end='\n'*2)
        if args.verbosity >= 3:
                print('track_groups =', work.trackgroups, end='\n'*2)

