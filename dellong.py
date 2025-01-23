"""Delete the recording with uuid from the long metadata file."""

import argparse
import shelve
import sys
from pathlib import Path

from common.constants import LONG

parser = argparse.ArgumentParser(
        prog=Path(sys.argv[0]).stem,
        description='Delete recording with uuid from long.')

parser.add_argument('uuid',
        help='delete recording with uuid')

args = parser.parse_args()

with shelve.open(str(LONG), 'c') as recording_shelf:
    try:
        del recording_shelf[args.uuid]
    except KeyError:
        print(f'recording not found: {args.uuid}')
        sys.exit(1)

